1.  In [Jupyter terminal](https://instructorqdznxgjnvrih.coursera-apps.org/terminals/1):
    ```bash
    cd notebooks && \
    git fetch origin && \
    git stash && \
    git merge --ff-only origin/coursera && \
    git -c core.fileMode=false stash pop
    ```
2.  Locally:
    ```bash
    git checkout coursera && \
    git pull && \
    git branch -f coursera-deployed coursera && \
    git push origin coursera-deployed
    ```
3.  Follow [this link](https://www.coursera.org/teach/practical-rl/content/edit/notebook/nqlp0/workspace) and click "Publish Workspace".
