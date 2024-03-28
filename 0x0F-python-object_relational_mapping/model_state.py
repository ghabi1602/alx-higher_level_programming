#!/usr/bin/python3
"""contains the class definition of a state"""

from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base

mymetadata = Metadata()
Base = declarative_base(metadata=mymeradata)

class State(Base):
    """class State definition"""
    __tablename__ = "states"
    id = Column(unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
