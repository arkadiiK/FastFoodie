from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cuisine = Column(String)
    address = Column(String)
    rating = Column(Float)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)


class Review(Base):
    __tablename__ = 'reviews'

    restaurant_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    rating = Column(Integer)
    comment = Column(String)