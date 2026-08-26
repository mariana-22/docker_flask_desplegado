FROM python:3.8-slim-buster

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python", "sample_app.py"]