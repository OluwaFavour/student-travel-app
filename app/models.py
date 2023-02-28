from sqlalchemy import Column, Date, DateTime, Integer, LargeBinary, String
from sqlalchemy.sql import func

from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=True)
    date_of_birth = Column(Date, nullable=False)
    country_of_birth = Column(String, nullable=False)
    country_of_residence = Column(String, nullable=False)   
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    profile_picture = Column(LargeBinary, nullable=True)
    date_created = Column(DateTime, server_default=func.now())