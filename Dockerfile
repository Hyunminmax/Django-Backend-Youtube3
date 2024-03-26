FROM python:3.11
LABEL maintainer="hyunmin"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get install -y build-essential libpq-dev musl-dev zlib1g zlib1g-dev linux-headers-$(uname -r) &&\
    if [ $DEV = "true" ] ; \
        then echo "--DEV BUILD--" && /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    apt-get remove -y --purge build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]