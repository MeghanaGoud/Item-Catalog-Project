#!/usr/bin/env python
import sys
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # return the json data
    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return{
            'id': self.id,
            'name': self.name,
            }


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(400))
    Cat_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return{
            'categories': self.categories.name,
            'id': self.id,
            'name': self.name,
            'description': self.description,
            }


engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)
