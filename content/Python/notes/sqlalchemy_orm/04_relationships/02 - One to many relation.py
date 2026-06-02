from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Null
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload
from sqlalchemy.exc import NoResultFound

database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

engine = create_engine(DATABASE_URI)
Base = declarative_base()

class School(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('Student', back_populates='school')

    def __repr__(self):
        return f'{self.id}-{self.name}\n'

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id'))
    school = relationship('School', back_populates='students')

    def __repr__(self):
        school_name = self.school.name if self.school else 'No assigned school'
        return f'{self.id}-{self.name}-{school_name}\n'

Base.metadata.create_all(engine)

def add_school(name):
    with Session(engine) as session:
        session.add(School(name=name))
        session.commit()

def add_student(name, school_id=Null()):
    with Session(engine) as session:
        session.add(Student(name=name, school_id=school_id))
        session.commit()

def get_all_schools():
    with Session(engine) as session:
        return session.query(School).options(joinedload(School.students)).order_by(School.id).all()

def get_all_students():
    with Session(engine) as session:
        return session.query(Student).options(joinedload(Student.school)).order_by(Student.id).all()

def update_student(student_id, new_name):
    with Session(engine) as session:
        try:
            student = session.query(Student).filter(Student.id == student_id).one()
            student.name = new_name
            session.commit()
        except NoResultFound:
            print(f'Student with ID {student_id} does not exist.')

def delete_student(student_id):
    with Session(engine) as session:
        try:
            student = session.query(Student).filter(Student.id == student_id).one()
            session.delete(student)
            session.commit()
        except NoResultFound:
            print(f'Student with ID {student_id} does not exist.')

# Example data.
# add_school('General Secondary School')
# add_school('Technical Secondary School of IT')
# add_student('Monica', 1)
# add_student('Todd', 1)
# add_student('Mark', 2)
# add_student('Robert', 2)
# add_student('Tom')

print(get_all_schools())
print(get_all_students())

schools = get_all_schools()
for school in schools:
    print(f'School: {school.id}.{school.name}')
    for student in school.students:
        print(f'\tStudent - {student.id} - {student.name}')

update_student(1, 'Tony')
delete_student(3)
