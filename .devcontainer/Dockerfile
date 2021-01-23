FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        python3-setuptools \
        locales locales-all \
        ffmpeg

# set timezone to Europ/Berlin
RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

RUN pip3 install --upgrade pip
RUN pip3 install awscli
RUN pip3 install boto3

WORKDIR /root
RUN wget https://github.com/DanielSWolf/rhubarb-lip-sync/releases/download/v1.10.0/rhubarb-lip-sync-1.10.0-linux.zip
RUN unzip rhubarb-lip-sync-1.10.0-linux.zip


