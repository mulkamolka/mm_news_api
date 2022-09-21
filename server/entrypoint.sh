#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 3306; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"