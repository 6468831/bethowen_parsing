FROM python:3.10-bullseye

WORKDIR /app

COPY . /app/

RUN python3 -m pip install -r requirements.txt

RUN apt -y update && apt -y upgrade && apt-get install -y wget unzip && \
    apt-get install -y apt-transport-https && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y -f ./google-chrome-stable_current_amd64.deb

CMD ["python", "parsing.py"]
