from fortress_alchemy import FortressAlchemy
from sqlalchemy import MetaData, Table, Column, Integer, String

# Create a FortressAlchemy instance
fortress_alchemy = FortressAlchemy(
    "orgId",
    "apiKey",
)

# Setup
engine = fortress_alchemy.create_engine("client1", echo=True)
metadata = MetaData()

# Define table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

# Create table
metadata.create_all(engine)

# Insert data
with engine.connect() as conn:
    conn.execute(
        users.insert(), [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    )

# Query data
with engine.connect() as conn:
    result = conn.execute(users.select())
    for row in result:
        print(row)
