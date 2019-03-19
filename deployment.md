1.  Locally:
    ```bash
    git checkout coursera && \
    git pull && \
    git bundle create github.bundle coursera-deployed..coursera

    # upload `github.bundle` via Jupyter interface in Instructor workspace next to `notebooks/`
    # URL: https://instructorqdznxgjnvrih.coursera-apps.org/tree

    rm github.bundle
    ```
2.  In [Jupyter terminal](https://instructorqdznxgjnvrih.coursera-apps.org/terminals/1):
    ```bash
    cd notebooks && \
    git fetch bundle && \
    rm ../github.bundle && \
    git stash && \
    git merge --ff-only bundle/coursera && \
    git -c core.fileMode=false stash pop
    ```
3.  Locally:
    ```bash
    git branch -f coursera-deployed coursera && \
    git push origin coursera-deployed
    ```
4.  Follow [this link](https://www.coursera.org/teach/practical-rl/content/edit/notebook/nqlp0/workspace) and click "Publish Workspace".
