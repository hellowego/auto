#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

BaseModel = declarative_base()

engine = create_engine('mysql://auto:auto@localhost:3306/auto',connect_args={'charset':'utf8'})
#engine = create_engine('mysql://auto:auto@54.179.147.230:3306/auto',connect_args={'charset':'utf8'})
DBSession = sessionmaker(bind=engine)


if __name__ == "__main__":
	print 'hi'