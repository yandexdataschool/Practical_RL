1.  Locally:
    ```bash
    git checkout coursera && \
    git pull && \
    git bundle create github.bundle coursera-deployed..coursera

    # upload `github.bundle` via Jupyter interface in Instructor workspace next to `notebooks/`

    rm github.bundle
    ```
2.  In Jupyter terminal:
    ```bash
    cd notebooks && \
    git fetch bundle && \
    rm ../github.bundle && \
    git stash && \
    git merge --ff-only bundle/coursera && \
    git stash pop
    ```
3.  Locally:
    ```bash
    git branch -f coursera-deployed coursera && \
    git push origin coursera-deployed
    ```
