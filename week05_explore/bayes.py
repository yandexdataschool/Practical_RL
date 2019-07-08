"""
A single-file module that makes your lasagne network into a bayesian neural net.
Originally created by github.com/ferrine , rewritten by github.com/justheuristic for simplicity

See example in the notebook
"""

import numpy as np

from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams

import lasagne
from lasagne import init
from lasagne.random import get_rng

from functools import wraps

__all__ = ['NormalApproximation', 'get_var_cost', 'bbpwrap']


class NormalApproximation(object):
    def __init__(self, mu=0, std=np.exp(-3), seed=None):
        """
        Approximation that samples network weights from factorized normal distribution.

        :param mu: prior mean for gaussian weights
        :param std: prior std for gaussian weights
        :param seed: random seed
        """
        self.prior_mu = mu
        self.prior_std = std
        self.srng = RandomStreams(seed or get_rng().randint(1, 2147462579))

    def log_normal(self, x, mean, std, eps=0.0):
        """computes log-proba of normal distribution"""
        std += eps
        return - 0.5 * np.log(2 * np.pi) - T.log(T.abs_(std)) - \
            (x - mean) ** 2 / (2 * std ** 2)

    def log_prior(self, weights):
        """
        Logarithm of prior probabilities for weights:
        log P(weights) aka log P(theta)
        """
        return self.log_normal(weights, self.prior_mu, self.prior_std)

    def log_posterior_approx(self, weights, mean, rho):
        """
        Logarithm of ELBO on posterior probabilities:
        log q(weights|learned mu and rho) aka log q(theta|x)
        """
        std = T.log1p(T.exp(rho))  # rho to std
        return self.log_normal(weights, mean, std)

    def __call__(self, layer, spec, shape, name=None, **tags):
        # case when user uses default init specs
        assert tags.get(
            'variational', False), "Please declare param as variational to avoid confusion"

        if not isinstance(spec, dict):
            initial_rho = np.log(np.expm1(self.prior_std))  # std to rho
            assert np.isfinite(initial_rho), "too small std to initialize correctly. Please pass explicit"\
                " initializer (dict with {'mu':mu_init, 'rho':rho_init})."
            spec = {'mu': spec, 'rho': init.Constant(initial_rho)}

        mu_spec, rho_spec = spec['mu'], spec['rho']

        rho = layer.add_param(
            rho_spec, shape, name=(
                name or 'unk') + '.rho', **tags)
        mean = layer.add_param(
            mu_spec, shape, name=(
                name or 'unk') + '.mu', **tags)

        # Reparameterization trick
        e = self.srng.normal(shape, std=1)
        W = mean + T.log1p(T.exp(rho)) * e

        # KL divergence KL(q,p) = E_(w~q(w|x)) [log q(w|x) - log P(w)] aka
        # variational cost
        q_p = T.sum(
            self.log_posterior_approx(W, mean, rho) -
            self.log_prior(W)
        )

        # accumulate variational cost
        layer._bbwrap_var_cost += q_p
        return W


def get_var_cost(layer_or_layers, treat_as_input=None):
    """
    Returns total variational cost aka KL(q(theta|x)||p(theta)) for all layers in the network

    :param layer_or_layers: top layer(s) of your network, just like with lasagne.layers.get_output
    :param treat_as_input: don't accumulate over layers below these layers. See same param for lasagne.layers.get_all_layers

    Alternatively, one can manually get weights for one layer via layer.get_var_cost()
    """
    cost = 0
    for layer in lasagne.layers.get_all_layers(
            layer_or_layers, treat_as_input):
        if hasattr(layer, 'get_var_cost'):
            # if layer is bayesian or pretends so
            cost += layer.get_var_cost()
    return cost


def bbpwrap(approximation=NormalApproximation()):
    """
    A decorator that makes arbitrary lasagne layer into a bayesian network layer:
    BayesDenseLayer = bbwrap()(DenseLayer)
    or more verbosely,
    @bbpwrap(NormalApproximation(pstd=0.01))
    BayesDenseLayer(DenseLayer):
        pass

    """

    def decorator(cls):
        def add_param_wrap(add_param):
            @wraps(add_param)
            def wrapped(self, spec, shape, name=None, **tags):
                # we should take care about some user specification
                # to avoid bbp hook just set tags['variational'] = True
                if not tags.get('trainable', True) or \
                        tags.get('variational', False):
                    return add_param(self, spec, shape, name, **tags)
                else:
                    # we declare that params we add next
                    # are the ones we need to fit the distribution
                    # they don't need to be regularized, strictly
                    tags['variational'] = True
                    tags['regularizable'] = False
                    param = self.approximation(self, spec, shape, name, **tags)
                    return param
            return wrapped

        def get_var_cost(self):
            """
            Returns total variational cost aka KL(q(theta|x)||p(theta)) for this layer.
            Alternatively, use function get_var_cost(layer) to get total cost for all layers below this one.
            """
            return self._bbwrap_var_cost

        cls.approximation = approximation
        cls._bbwrap_var_cost = 0
        cls.add_param = add_param_wrap(cls.add_param)
        cls.get_var_cost = get_var_cost
        return cls

    return decorator
