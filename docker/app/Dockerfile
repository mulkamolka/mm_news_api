FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc jq libc-dev

COPY . ./

RUN jq -r '.default \
    | to_entries[]  \
    | .key + .value.version' \
    Pipfile.lock > requirements.txt && \
    pip install -r requirements.txt

ENV HOST=0.0.0.0
ENV PORT=8000
ENV DOT_ENV=development

CMD ["sh", "-c",  "uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]