import signal
import sys

import sqlalchemy as db

from sqlalchemy.orm import sessionmaker
from flats_project.config import config

connection_string = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
engine = db.create_engine(connection_string)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


def close_database_connection(signal, frame):
    engine.dispose()  # Dispose the connection pool
    sys.exit(0)


signal.signal(signal.SIGINT, close_database_connection)
signal.signal(signal.SIGTERM, close_database_connection)
