from website import db
from website.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///database.db")

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# users = get_users(session

user = User(email="norsh@gmail.com",
            password="password1", first_name="Norsh")
db.session.add(user)
db.session.commit()
