from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import and_ , or_, not_

Session = sessionmaker(bind=engine)
session = Session()
users = session.query(User).all()


for user in users:
    print(f"Username: {user.username}, Password: {user.password}") 