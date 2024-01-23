import sqlalchemy as db

# PostgreSQL Configuration
POSTGRES_DB = "sreality"
POSTGRES_USER = "myuser"
POSTGRES_PASSWORD = "mypassword"
POSTGRES_HOST = "postgres-db"  # Using Docker service name as host
POSTGRES_PORT = "5432"

# Create the connection string
connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create the engine
engine = db.create_engine(connection_string)

# Connect to the database
conn = engine.connect()

# Now you can use `conn` to execute queries, for example:
# result = conn.execute("SELECT * FROM my_table")
# for row in result:
#     print(row)

# Don't forget to close the connection when you're done
conn.close()