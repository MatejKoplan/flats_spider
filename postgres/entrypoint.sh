#!/bin/bash
set -e

# Enable data checksums
if [ ! -d "/var/lib/postgresql/data" ]; then
    /usr/lib/postgresql/xx/bin/initdb -D /var/lib/postgresql/data -k
fi

# Call the original entrypoint script
exec docker-entrypoint.sh "$@"
