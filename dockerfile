FROM python:3.10

WORKDIR /app

COPY . /app/

RUN python3 -m pip install -r requirements.txt

RUN apt -y update && apt -y upgrade && apt-get install -y wget unzip && \
    apt-get install -y apt-transport-https && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

CMD ["python", "parsing.py"]
