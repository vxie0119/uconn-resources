# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
# FROM python:3.11-slim-bookworm
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN mkdir test
COPY . ./test

# EXPOSE 5000

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "flask", "run" , "--host", "0.0.0.0", "--port", "5000"]
