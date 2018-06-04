from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os


sql_path = os.getcwd() + '/sql/sodiq.db'

engine = create_engine(
    "sqlite:///" + sql_path
)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))
Mode = declarative_base()
Mode.query = db_session.query_property()

def init_db():
    import lib.models
    Mode.metadata.create_all(bind=engine)

