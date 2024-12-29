from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import and_ , or_, not_

Session = sessionmaker(bind=engine)
session = Session()

# we will learn filtering 
#users=session.query(User).filter(User.username.like("%anush%")).all()  # it will filter the users with username containing anush
#users=session.query(User).filter(User.username=="anushka").all()  # it will filter the users with username starting with anush

#now we will use filter_by
#users=session.query(User).filter_by(username="anushka").all() # it will give lisy of all the users with username anushka, we can insert more after username it will be treated as and condition 

# now we will use where()
#users = session.query(User).where(User.username=="anushka", User.password=="anushka123").all()  # it will give lisy of all the users with username anushka, we can insert more after username it will be treated as and condition

# we can use or_() and not_() also with where()
users = session.query(User).where(or_(User.username=="anushka", User.password=="anushka123")).all()  # it will give lisy of all the users with username anushka or password anushka123



for user in users:
    print(f"Username: {user.username}, Password: {user.password}") 