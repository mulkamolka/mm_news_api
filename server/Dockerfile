# pull python image
FROM python:3.9-alpine3.13

# set up environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFRED 1

# set up working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install system dependencies
RUN apk add gcc jq libc-dev g++

# copy the project folder to the container
COPY . ./

RUN jq -r '.default \
    | to_entries[]  \
    | .key + .value.version' \
    Pipfile.lock > requirements.txt && \
    pip install -r requirements.txt

# wait until the database starts
COPY ./entrypoint.sh .

RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
