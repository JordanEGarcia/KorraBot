FROM ubuntu:20.04
ARG TOKEN_VALUE= "Please insert a token"
ENV TOKEN_VALUE=${TOKEN_VALUE}
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    ffmpeg
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["bash", "startup.sh"]
