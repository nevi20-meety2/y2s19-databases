from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rating):
	new_article = Knowledge(
		name = name,
		topic = topic,
		rating = rating)
	session.add(new_article)
	session.commit()
	

def query_all_articles():
	articles = session.query(Knowledge).all()
	print(articles)

query_all_articles()

def query_article_by_topic(topic):
	bytopic = session.query(Knowledge).filter_by(topic=topic).all()

	return bytopic
print (query_article_by_topic("Boy Bands"))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

delete_article_by_topic("Supernatural")

def delete_all_articles():
	pass

def edit_article_rating():
	pass


# add_article("One Direction", "Boy Bands", 10)
# add_article("Vampires", "Supernatural", 5)
# add_article("Heart", "Human Body", 8)