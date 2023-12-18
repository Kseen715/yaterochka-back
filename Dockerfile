FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

ENV NAME="none"
ENV HOST="none"
ENV PORT="none"
ENV PASSWORD="none"
ENV USER="none"

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver "0.0.0.0:8000" NAME=${NAME} HOST=${HOST} PORT=${PORT} PASSWORD=${PASSWORD} USER=${USER}
