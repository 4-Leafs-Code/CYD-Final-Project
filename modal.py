from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User:
   def __init__(self, id_num, full_name, username, password, site_administrator, facility_administrator, email, alt_email):
      self.id_num = id_num,
      self.full_name = full_name,
      self.username = username,
      self.password = password,
      self.site_administrator = site_administrator,
      self.facility_administrator = facility_administrator,
      self.email = email,
      self.alt_email = alt_email

