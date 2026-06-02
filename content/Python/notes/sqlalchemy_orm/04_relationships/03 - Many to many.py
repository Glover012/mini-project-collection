from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload

# Database connection parameters.
database_name = 'sqlalchemy'
DATABASE_URI = f'postgresql+psycopg2://postgres:admin@localhost/{database_name}'

# Creates the database engine and the base class for ORM table models.
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Many-to-many relationship example.
# A many-to-many relationship can connect blog articles with tags.
# To define this relationship, SQLAlchemy needs an association table.

# Defines the association table.
# It stores foreign keys from both related tables.
article_tags = Table(
    'article_tags',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)

    # In a many-to-many relationship, secondary points to the association table.
    # The association table stores foreign keys from both related tables.
    tags = relationship('Tag', secondary=article_tags, back_populates='articles')

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Uses the same association table to access articles assigned to each tag.
    articles = relationship('Article', secondary=article_tags, back_populates='tags')

Base.metadata.create_all(engine)

def add_article_with_tags(title, content, tag_names):
    with Session(engine) as session:
        article = Article(title=title, content=content)

        for tag_name in tag_names:
            # Checks whether the tag already exists in the database.
            tag = session.query(Tag).filter_by(name=tag_name).first()

            # Creates the tag if it does not exist yet.
            if not tag:
                tag = Tag(name=tag_name)

            # Adds the tag to the article.
            # SQLAlchemy also creates the matching row in the association table.
            article.tags.append(tag)

        session.add(article)
        session.commit()

def get_all_articles():
    with Session(engine) as session:
        # joinedload loads related tags in the same query context.
        # This reduces the number of additional queries needed later.
        articles = session.query(Article).options(joinedload(Article.tags)).all()
        return articles

def add_tags_if_not_exists(tag_names):
    with Session(engine) as session:
        for tag_name in tag_names:
            if not session.query(Tag).filter_by(name=tag_name).first():
                session.add(Tag(name=tag_name))
        session.commit()

# Adds example articles.
# add_article_with_tags('Quantum computing', 'content', ['IT', 'Science', 'Physics', 'Electronics'])
# add_article_with_tags('Niagara Falls', 'content', ['Nature'])
# add_article_with_tags('Most popular engines of all time', 'content', ['Mechanics', 'Cars', 'Engines'])

# Adds example tags.
# add_tags_if_not_exists(['Python', 'SQL', 'SQLAlchemy'])
# add_tags_if_not_exists(['Nature'])
# add_tags_if_not_exists(['Comedy'])

def print_articles_with_tags(articles):
    for article in articles:
        print(f'{article.id}| {article.title}| {article.content}')
        print('Tags:')
        for tag in article.tags:
            print(f'{tag.id}-{tag.name}')
        print()

def print_articles_with_tags_as_list(articles):
    for article in articles:
        tags = [f'{tag.id}-{tag.name}' for tag in article.tags]
        print(f'{article.id}| {article.title}| {article.content}')
        print(tags)

all_articles = get_all_articles()
print_articles_with_tags_as_list(all_articles)
