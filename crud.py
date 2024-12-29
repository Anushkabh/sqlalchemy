from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()
#user= User(username="anushka", password="anushka123")
#user_2= User(username="anushkad", password="anushka12d3")
#user_3= User(username="acnushka", password="anushka12c3")
#session.add(user)
#session.add_all([user_2, user_3])
#session.commit()

#now we will see how we can read from the database

#users=session.query(User).all()
#print(users[0].username)

#for user in users:
    #print(f"Username: {user.username}, Password: {user.password}")

users=session.query(User).filter_by(username="anushka").all() # it will give lisy of all the users with username anushka
# we can use one_or_none() to get only one user with the username anushka and if there is no user with the username anushka then it will return None  .first() will return the first user with the username anushka
print(users)

#we can update the table
#user=session.query(User).filter_by(username="anushka").first()
#user.password="anushka1234"
#session.commit()

#we can delete the user
#user=session.query(User).filter_by(username="anushka").first()
#session.delete(user)
#session.commit()
