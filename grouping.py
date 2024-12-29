from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import func
#what is func ?
#func is a class in sqlalchemy which is used to call the sql functions like count, sum, avg etc

Session = sessionmaker(bind=engine)
session = Session()
users = session.query(User.username, func.count(User.id)).group_by(User.password).all()
# sample output
# [('anushka', 1), ('anushka', 1), ('anushka', 1)]

users_tuple= (session.query(User.username, func.count(User.id)).filter(User.username=="anushka").group_by(User.password).all() )
# sample output
# [('anushka', 1), ('anushka', 1), ('anushka', 1)]

# conditionsl chaining






for user in users:
    print(f"Username: {user.username}, Password: {user.password}")