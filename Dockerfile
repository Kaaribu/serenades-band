# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]