FROM python:3.8

WORKDIR /home/ubuntu/assignment

COPY myserver.py .

CMD ["python", "myserver.py"]

