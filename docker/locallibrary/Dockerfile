FROM python:latest

COPY locallibrary/requirements.txt /
RUN pip install -r requirements.txt

COPY ./docker/locallibrary/docker-entrypoint.sh ./docker/locallibrary/wait-for-command.sh ./docker/locallibrary/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

WORKDIR /usr/app


ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["sh /runserver.sh"]

