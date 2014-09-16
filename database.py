from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Watcher(Base):
	__tablename__ = 'watcher'
	id = Column(Integer, primary_key=True)
	email = Column(String, nullable=False)

class Node(Base):
	__tablename__= 'node'
	id = Column(Integer, primary_key=True)
	url = Column(String, nullable=False)

def init():
	db = create_engine('sqlite:///websight.db')
	Base.metadata.create_all(db)
	return db