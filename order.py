from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# we will learn order by 
users= session.query(User).order_by(User.username.desc).all()  # it will order the users by username

for user in users:
    print(f"Username: {user.username}, Password: {user.password}")