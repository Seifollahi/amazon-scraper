from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text, SmallInteger)
from scrapy.utils.project import get_project_settings


Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """

    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Products(Base):
    __tablename__ = "amazonbestsellers"


    selected_department = Column('selected_department', String(150))
    product_title = Column('product_title', String(500))
    rank = Column('rank', SmallInteger)
    rating = Column('rating', SmallInteger)
    number_of_ratings = Column('number_of_ratings', Integer)
    product_reviews_url = Column('product_reviews_url', String(250))
    price = Column('price', String(50))
    date = Column('date', DateTime,default=datetime.datetime.utcnow)
