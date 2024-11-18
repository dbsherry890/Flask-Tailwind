from website import db
from website.models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db")

Session = sessionmaker(bind=engine)
session = Session()

user = User(email="norsh@gmail.com",
            password="password1", first_name="Norsh")

new_user = user
db.session.add(new_user)
db.session.commit()
