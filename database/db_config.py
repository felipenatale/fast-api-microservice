from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import config
from contextlib import contextmanager

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db_session():

    engine = create_engine(        
        config.MYSQL_URI,
        pool_pre_ping=True,
        echo=False,
        pool_size=10, 
        max_overflow=20
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = create_db_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()