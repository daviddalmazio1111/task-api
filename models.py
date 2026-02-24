from sqlalchemy import Column , Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__="Tasks"

    id=Column(Integer,primary_key=True,index=True)
    task=Column(String)
    owner=Column(String)