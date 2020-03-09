FROM python:3

RUN apt-get update && apt-get install -y vim

WORKDIR /map-function
COPY src .
WORKDIR /map-function/src
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "foo.wsgi"] 
