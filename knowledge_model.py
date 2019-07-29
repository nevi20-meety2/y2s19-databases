from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):

   __tablename__ = 'Knowledge'
   article_id = Column(Integer, primary_key=True)
   name = Column(String)
   topic = Column(String)
   rating = Column(Integer)

def __repr__(self):
	return ("Article Name: {}\n"
			"Article Topic: {}\n"
			"Rating: {}\n"
			"ID: {}").format(
				self.name,
				self.topic,
				self.rating,
				self.article_id)

	