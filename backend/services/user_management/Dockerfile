FROM python:3.11.4-slim-buster

WORKDIR /user_management

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . /user_management

RUN pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["python", "manage.py", "runserver_plus", "--key-file", "selftest-key", "--cert-file", "selftest-cert", "0.0.0.0:8000"]
