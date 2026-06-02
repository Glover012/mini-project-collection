from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, validates
from datetime import datetime

# SQLAlchemy validators can check values before they are saved.

database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

engine = create_engine(DATABASE_URI)
Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    # nullable=False means this column must receive a value.
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    max_speed = Column(Integer)
    color = Column(String)

    def __repr__(self):
        return (f"REPR - Car(id={self.id}, brand='{self.brand}', "
                f"model='{self.model}', year={self.year}, "
                f"max_speed={self.max_speed}, color='{self.color}')\n")

    def __str__(self):
        return (f"STR - Car(id={self.id}, brand='{self.brand}', "
                f"model='{self.model}', year={self.year}, "
                f"max_speed={self.max_speed}, color='{self.color}')\n")

    @validates('year')
    def validate_year(self, key, year):
        current_year = datetime.now().year
        if year > current_year or year < 1900:
            raise ValueError('Production year must be between 1900 and the current year.')
        return year

    @validates('max_speed')
    def validate_max_speed(self, key, max_speed):
        if max_speed < 0 or max_speed > 400:
            raise ValueError('Max speed must be between 0 and 400 km/h.')
        return max_speed

    @validates('color')
    def validate_color(self, key, color):
        if not color:
            raise ValueError('Color must be set.')
        return color

Base.metadata.create_all(engine)

def add_car(brand, model, year, max_speed, color):
    with Session(engine) as session:
        try:
            new_car = Car(brand=brand, model=model, year=year, max_speed=max_speed, color=color)
            session.add(new_car)
            session.commit()
        except ValueError as e:
            print(f'Error while adding car: {e}')
            session.rollback()

def get_all_cars():
    with Session(engine) as session:
        return session.query(Car).all()

def get_car_by_id(car_id):
    with Session(engine) as session:
        return session.query(Car).filter(Car.id == car_id).one()

# Valid example records.
# add_car('Toyota', 'Corolla', 2020, 180, 'Red')
# add_car('Dodge', 'Charger', 1969, 190, 'Orange')

# Invalid example records.
add_car('Ford', 'Mustang', 2080, 500, '')
add_car('Ford', 'Mustang', 2010, 500, '')
add_car('Ford', 'Mustang', 2010, 280, '')

print(get_all_cars())
print(get_car_by_id(1))
