FROM postgres:latest

# Add init scripts, that will be run the first time - when volume in empty.
COPY init /docker-entrypoint-initdb.d

CMD ["postgres"]