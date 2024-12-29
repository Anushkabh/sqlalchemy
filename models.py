from sqlalchemy import Column, Integer,String, create_engine
from sqlalchemy.orm import declarative_base


engine=create_engine('sqlite:///data.db')  # third slash for relative path to the current directory where the script is running from and not the root directory 4th slash is for absolute path to the root directory

Base=declarative_base() 


class User(Base):  # class to create the table
    __tablename__='users'
    id=Column(Integer, primary_key=True)
    username=Column(String(80), unique=True)
    password=Column(String(80))

Base.metadata.create_all(engine)  # creates the table in the database
