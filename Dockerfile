FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY hacker_news_data.json ./
COPY tast1_job.py ./

CMD [ "python", "./task1_job.py"]
