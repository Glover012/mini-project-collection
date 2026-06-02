# SQLAlchemy is an ORM (Object Relational Mapper) that makes working with databases easier.
# Instead of writing raw SQL queries directly, Python classes and objects are mapped to database tables and rows.
# This can reduce repetitive code and lower the risk of simple query mistakes.

# CRUD operations - create, read, update and delete - can be handled through the ORM.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

database_name = 'sqlalchemy'

# Database connection parameters.
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

# Creates the database engine used to communicate with PostgreSQL.
engine = create_engine(DATABASE_URI)

# Creates the base class for all ORM table models.
# Models inherit from Base and define table structures declaratively.
Base = declarative_base()

# Defines a table model.
# ExampleTable inherits from Base and represents one table in the database.
class ExampleTable(Base):
    __tablename__ = 'example_table'  # Database table name.

    id = Column(Integer, primary_key=True)  # Primary key column.
    name = Column(String)
    description = Column(String)

# Creates the database table based on the defined model.
Base.metadata.create_all(engine)

# Adds a new record to the table.
# Session manages database operations such as adding, updating and deleting records.
with Session(engine) as session:
    new_record = ExampleTable(name='Example', description='Example description')
    session.add(new_record)  # Adds the record to the session.
    session.commit()  # Saves the changes to the database.

# Fetches and prints all records from the table.
with Session(engine) as session:
    result = session.query(ExampleTable).all()
    for row in result:
        print(f'ID:{row.id}, Name:{row.name}, Description:{row.description}')
