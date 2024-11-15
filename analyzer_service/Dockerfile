FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
WORKDIR /analyzer_service
COPY requirements.txt /analyzer_service/
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python manage.py makemigrations \
    python manage.py migrate
COPY . .    