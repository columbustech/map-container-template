FROM python:3

RUN apt-get update && apt-get install -y vim

WORKDIR /map-function
COPY . /map-function
RUN pip install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /map-function/src

EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
