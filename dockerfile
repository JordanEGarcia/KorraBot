FROM python:3.9-alpine
ARG TOKEN_VALUE= "Please insert a token"
ENV TOKEN_VALUE=${TOKEN_VALUE}
RUN apk update && apk add bash
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "startup.sh"]