FROM python:3.8-alpine
LABEL maintainer="Galen Guyer <galen@galenguyer.com>"

RUN apk add tzdata && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo 'America/New_York' > /etc/timezone && \
    apk del tzdata

RUN pip install pipenv
WORKDIR /opt/demo/
ADD Pipfile Pipfile.lock /opt/demo/
RUN pipenv install
ADD . /opt/demo/

ENTRYPOINT [ "pipenv", "run", "gunicorn", "infod:app" ]
CMD [ "--bind=0.0.0.0:8080", "--access-logfile=-" ]
