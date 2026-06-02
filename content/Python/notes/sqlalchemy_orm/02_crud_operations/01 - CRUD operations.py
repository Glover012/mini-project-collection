# CRUD operations: create, read, update and delete.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

# Database connection parameters.
database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

# Creates the database engine and the base class for ORM table models.
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Defines the users table model.
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)

# Creates the table in the database based on the model definition.
Base.metadata.create_all(engine)

# Creates a new user.
def add_user(username, email):
    with Session(engine) as session:
        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()

# Reads all users ordered by username.
def get_all_users():
    with Session(engine) as session:
        users = session.query(User).order_by(User.username).all()
        return users

# Prints users in the console.
def print_all_users(users):
    for user in users:
        print(f'ID:{user.id}, Username:{user.username}, Email:{user.email}')

# Updates an existing user.
def update_user(user_id, new_username, new_email):
    with Session(engine) as session:
        user_to_update = session.query(User).filter(User.id == user_id).one()
        user_to_update.username = new_username
        user_to_update.email = new_email
        session.commit()

# Deletes one user by id.
def delete_user(user_id):
    with Session(engine) as session:
        user_to_delete = session.query(User).filter(User.id == user_id).one()
        session.delete(user_to_delete)
        session.commit()

# Deletes all users.
def delete_all_users():
    with Session(engine) as session:
        session.query(User).delete()
        session.commit()

# Deletes all users.
# delete_all_users()

# Adds example users.
# add_user('Tom', 'tom@example.com')
# add_user('Ann', 'ann@example.com')
# add_user('Rob', 'rob@example.com')

# Displays users.
print('All users:')
print_all_users(get_all_users())

# Updates a user.
update_user(17, 'Tom_updated', 'tom_updated@example.com')

# Displays users after the update.
print('All users after update:')
print_all_users(get_all_users())

# Deletes a user.
delete_user(18)

# Displays users after deleting one user.
print('All users after deleting user id 18:')
print_all_users(get_all_users())
