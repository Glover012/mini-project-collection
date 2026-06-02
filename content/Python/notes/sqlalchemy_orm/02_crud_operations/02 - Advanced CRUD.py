from sqlalchemy import create_engine, Column, Integer, String, and_, or_
from sqlalchemy.orm import declarative_base, Session

# Advanced CRUD examples using SQLAlchemy query filters.

# Database connection parameters.
database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

# Creates the database engine and the base class for ORM table models.
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Defines the employees table model.
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f'{self.id}-{self.name}-{self.department}-{self.age}'

# Creates the table in the database based on the model definition.
Base.metadata.create_all(engine)

# Creates a new employee.
def add_employee(name, department, age):
    with Session(engine) as session:
        new_employee = Employee(name=name, department=department, age=age)
        session.add(new_employee)
        session.commit()

# Reads all employees.
def get_all_employees():
    with Session(engine) as session:
        employees = session.query(Employee).all()
        return employees

# Updates an existing employee.
def update_employee(employee_id, new_name, new_department, new_age):
    with Session(engine) as session:
        employee_to_update = session.query(Employee).filter(Employee.id == employee_id).one()
        employee_to_update.name = new_name
        employee_to_update.department = new_department
        employee_to_update.age = new_age
        session.commit()

# Deletes one employee by id.
def delete_employee(employee_id):
    with Session(engine) as session:
        employee_to_delete = session.query(Employee).filter(Employee.id == employee_id).one()
        session.delete(employee_to_delete)
        session.commit()

# Finds employees that match both conditions.
def find_employees_by_criteria(department, age):
    with Session(engine) as session:
        employees = session.query(Employee).filter(
            and_(Employee.department == department, Employee.age > age)
        ).all()
        return employees

# Finds employees that match at least one condition.
def find_employees_by_name_or_department(name, department):
    with Session(engine) as session:
        employees = session.query(Employee).filter(
            or_(Employee.name == name, Employee.department == department)
        ).all()
        return employees

# Example data.
# add_employee('Tom', 'IT', 25)
# add_employee('Eric', 'IT', 28)
# add_employee('Ann', 'HR', 33)
# add_employee('Lisa', 'Management', 39)
# add_employee('Todd', 'Management', 41)

print(get_all_employees())
print(find_employees_by_criteria('HR', 18))
print(find_employees_by_name_or_department('Lisa', 'IT'))
