import signal
import sys

import sqlalchemy as db

from config import config

connection_string = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
engine = db.create_engine(connection_string)
connection = engine.connect()


def close_database_connection(_signal, _frame) -> None:
    engine.dispose()
    sys.exit(0)


# Dispose the connection pool on app exit
signal.signal(signal.SIGINT, close_database_connection)
signal.signal(signal.SIGTERM, close_database_connection)
