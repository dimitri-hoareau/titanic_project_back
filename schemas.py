from pydantic import BaseModel
from typing import Optional

class PassengerBase(BaseModel):
    PassengerId: int  
    Survived: Optional[bool]
    Pclass: Optional[int]
    Name: Optional[str]
    Sex: Optional[str]
    Age: Optional[float]
    SibSp: Optional[int]
    Parch: Optional[int]
    Ticket: Optional[str]
    Fare: Optional[float]
    Cabin: Optional[str]
    Embarked: Optional[str]

class PassengerCreate(PassengerBase):
    pass

class Passenger(PassengerBase):
    class Config:
        from_attributes = True


  