FROM python:3.10-alpine3.15
LABEL maintainer="kmilew"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django:django /vol && \
    chmod -R 755 /vol

ENV PATH="/venv/bin:$PATH"

USER django