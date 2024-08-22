from fortress_alchemy import FortressAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a FortressAlchemy instance
fortress_alchemy = FortressAlchemy(
    "orgId",
    "apiKey",
)

# Step 1: Define the database engine (using SQLite in-memory database for this example)
engine = fortress_alchemy.create_engine("client1", echo=True)

# Step 2: Define the base class for the model
Base = declarative_base()


# Step 3: Define the model (a table structure)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"


# Step 4: Create the table in the database
Base.metadata.create_all(engine)

# Step 5: Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Step 6: Add and commit new records to the database
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

# Step 7: Query the database
for user in session.query(User).all():
    print(user)
