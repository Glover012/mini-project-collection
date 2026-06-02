from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session
from tkinter import Tk, Label, Button
import random

# Simple Tkinter app that stores quotes with SQLAlchemy and displays a random quote.

database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

engine = create_engine(DATABASE_URI)
Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(engine)
    quotes = [
    'The journey of a thousand miles begins with a single step. - Lao Tzu',
    'I think, therefore I am. - René Descartes',
    'Stay hungry, stay foolish. - Steve Jobs',
    'That which does not kill us makes us stronger. - Friedrich Nietzsche',
    'It always seems impossible until it is done. - Nelson Mandela'
    ]

    with Session(engine) as session:
        if session.query(Quote).count() == 0:
            for quote_text in quotes:
                session.add(Quote(text=quote_text))
            session.commit()

def show_random_quote():
    with Session(engine) as session:
        quote_count = session.query(Quote).count()
        random_int = random.randint(1, quote_count)
        random_quote = session.execute(select(Quote).where(Quote.id == random_int)).scalar_one()
        quote_label.config(text=random_quote.text)

init_db()

root = Tk()
root.title('Random quote')
root.geometry('1024x768')

quote_label = Label(root, text='', wraplength=1000)
quote_label.pack(pady=20)

random_quote_button = Button(root, text='Get random quote', command=show_random_quote)
random_quote_button.pack(pady='30')

def on_closing():
    engine.dispose()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', on_closing)

show_random_quote()
root.mainloop()
