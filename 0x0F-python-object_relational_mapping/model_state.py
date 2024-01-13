#!/usr/bin/python3
"""
Module containing the definition of the State class.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    State class that represents a state in the database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# Replace 'your_username' and 'your_password'
# with your actual MySQL username and password
engine = create_engine('mysql://your_username:your_password@localhost:3306')
Base.metadata.create_all(engine)

