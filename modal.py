from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id_num = Column(Integer, primary_key=True)
    full_name = Column(String)
    username = Column(String)
    password = Column(String)
    site_administrator = Column(Boolean)
    facility_administrator = Column(Boolean)
    email = Column(String)
    alt_email = Column(String)

