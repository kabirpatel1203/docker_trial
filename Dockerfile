FROM python:3.9

WORKDIR /DOCKER_Trial

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]