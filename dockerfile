ARG TOKEN_VALUE
FROM python:3.9-alpine
RUN apk update && apk add bash
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN export TOKEN=$TOKEN_VALUE
ENTRYPOINT ["bash", "startup.sh"]