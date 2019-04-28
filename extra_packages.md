If you need to quickly install an extra Python package, such as `gym`, in your Coursera learner container:

1.  On your local machine, run the following command. If you want the latest version, replace `PACKAGE` with `gym`. If you want a specific version, use something like `gym==0.12.0`.
    ```bash
    pip3 download --python-version 36 --no-deps PACKAGE
    ```
    This will download the distribution version of your Python package into your current directory and print its name.
2.  Next, go to your container. It should have URL similar to `https://<long-random-string>.coursera-apps.org`.
3.  In the top-right corner, click "Upload", select the file you downloaded on your machine and upload it.
4.  In the top-right corner, click "New" → "Terminal".
5.  In the newly opened terminal, type
    ```bash
    pip3 install <package-filename>
    ```
