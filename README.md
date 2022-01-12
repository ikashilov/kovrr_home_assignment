## Kovrr Data Engineer Home Assignment
The assignment description is not included to this repository for the copyright reasons.
Both 2 tasks of this assignment can be run in [JupyterLab](https://jupyter.org/)


### Instalation process
1. Follow the [instalation guide](https://www.python.org/downloads/) to install Python.
2. Follow the [instalation guide](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) if you want to use Jupyter.
3. Run `pip3 install -r requirements.txt` to install the dependences. 

#### Task 1
If you do not want to install Jupyter on your machine you can use a pure Python for this task:
```bash
python3 task1_job.py [-h] [-i INPUT] [-o OUTPUT]
```

### Task 2
Open `task2_report.html` in your web browser.

### Task 3
It all depends on how our infrastructure is organized. Here are the few examples:
1. The most naive approach is to wrap the `job()` call into `while(time.sleep(24*3600))` loop ;)
2. The second approach is to use [cron](https://en.wikipedia.org/wiki/Cron)
3. If we run our apps in k8s we can use [CronJob](https://en.wikipedia.org/wiki/Cron)
4. We might run all our jobs in [Apache Airflow](https://airflow.apache.org/)
