from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

connection_string = 'postgresql+psycopg2://postgres:admin@localhost/flask'

Base = declarative_base()


def create_all_entities():
    Base.metadata.create_all(engine)


Session = sessionmaker()
engine = create_engine(connection_string, echo=True)
local_session = Session(bind=engine)