#!/usr/bin/python3
"""
contains state class also  Base a instance of a declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

itmetadata = MetaData()
Base = declarative_base(metadata=itmetadata)


class State(Base):
    """
    class with an id and name attributee of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
