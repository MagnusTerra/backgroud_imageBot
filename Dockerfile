FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    python3.10 \
    python3-pip \
    git 



RUN pip install rembg pytelegrambotapi


