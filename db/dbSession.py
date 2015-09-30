from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

BaseModel = declarative_base()
engine = create_engine('mysql://root:root@localhost:3306/auto')
DBSession = sessionmaker(bind=engine)


if __name__ == "__main__":
	print 'hi'