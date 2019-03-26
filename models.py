from flask import Flask

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atm.db'

db = SQLAlchemy(app)

#Building a ForeignKey. With Class Account.
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	accounts = db.relationship('Account', backref='user', lazy=True)


# Created an account to sql.
class Account(db.Model):

  id = db.Column(db.Integer, primary_key=True)

  account_number = db.Column(db.Integer, unique=True, nullable=False)

  pin = db.Column(db.Integer, unique=False, nullable=False)

  balance = db.Column(db.Integer)

  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  credit_card = db.Column(db.Integer)
  #--------------------------------------------------------




