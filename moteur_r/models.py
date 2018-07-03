from flask_sqlalchemy import SQLAlchemy
import logging as lg
import pandas as pd

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(200), nullable=False)
	gender = db.Column(db.Integer(), nullable=False)

	def __init__(self, description, gender):
		self.description = description
		self.gender = gender

def charge_df():
    FILE = 'datas/movie_metadata.csv'
    df = pd.read_csv(FILE)
    
    return df

#MA_BASE = charge_df()

def init_db():
	db.drop_all()
	db.create_all()
	db.session.add(Content("Super", 1))
	db.session.add(Content("Cool2", 0))
	db.session.add(Content("Toc is the best",1))
	db.session.commit()
	lg.warning('Database initialized !') 


######db.create_all()
