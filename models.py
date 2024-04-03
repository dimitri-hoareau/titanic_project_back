from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Passenger(Base):
    __tablename__ = 'passengers'

    PassengerId = Column(Integer, primary_key=True, index=True)
    Survived = Column(Boolean)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Float)
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String)
