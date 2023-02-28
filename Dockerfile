FROM python:3.9.11

WORKDIR /usr/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "run"]
