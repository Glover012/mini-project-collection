from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload

database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

engine = create_engine(DATABASE_URI)
Base = declarative_base()

# back_populates creates a two-way relationship between models.
# uselist=False means the relationship expects one related object.
class User2(Base):
    __tablename__ = 'users2'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    profile_relation = relationship('UserProfile', back_populates='user_relation', uselist=False)

    def __repr__(self):
        profile_picture = self.profile_relation.profile_picture if self.profile_relation else 'No profile'
        return f'{self.id} - {self.username} - {profile_picture}'

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users2.id'), unique=True)
    profile_picture = Column(String)
    user_relation = relationship('User2', back_populates='profile_relation')

Base.metadata.create_all(engine)

def add_user_with_profile(username, profile_picture):
    with Session(engine) as session:
        user = User2(username=username)
        user_profile = UserProfile(profile_picture=profile_picture, user_relation=user)
        session.add_all([user, user_profile])
        session.commit()

def get_all_users_with_profiles():
    with Session(engine) as session:
        return session.query(User2).options(joinedload(User2.profile_relation)).all()

def print_all_users_with_profiles(users):
    for user in users:
        profile_picture = user.profile_relation.profile_picture if user.profile_relation else 'No profile'
        print(f'{user.id} - {user.username} - {profile_picture}')

# add_user_with_profile('Tom', 'tom.jpg')
# add_user_with_profile('Ann', 'ann.jpg')
# add_user_with_profile('Jennifer', 'jennifer.jpg')

print(get_all_users_with_profiles())
