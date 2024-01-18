#!/bin/bash
set -e

# Perform SQL commands to set up the database
psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE USER myuser WITH PASSWORD 'mypassword';
    CREATE DATABASE sreality;
    GRANT ALL PRIVILEGES ON DATABASE sreality TO myuser;
EOSQL
