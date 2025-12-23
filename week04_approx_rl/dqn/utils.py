import psutil  # type: ignore


def is_enough_ram(min_available_gb=0.1):
    mem = psutil.virtual_memory()
    return mem.available >= min_available_gb * (1024**3)


def linear_decay(
    init_val: float, final_val: float, cur_step: int, total_steps: int
) -> float:
    if cur_step >= total_steps:
        return final_val
    return (init_val * (total_steps - cur_step) + final_val * cur_step) / total_steps
