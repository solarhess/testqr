import transaction
import uuid

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

from sqlalchemy.dialects.postgresql import \
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, INET, INTEGER, INTERVAL, \
    MACADDR, NUMERIC, REAL, SMALLINT, TEXT, TIME, TIMESTAMP, \
    UUID, VARCHAR
    
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class BusinessCard(Base):
    __tablename__ = 'businesscard'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(Unicode(255))
    company = Column(Unicode(255))
    phone_work = Column(Unicode(255))
    phone_mobile = Column(Unicode(255))
    phone_home = Column(Unicode(255))
    email = Column(Unicode(255), unique=True)

    def __init__(self, id, name, company, phone_work, phone_mobile, phone_home, email):
        self.id = id
        self.name = name
        self.company = company
        self.phone_work = phone_work
        self.phone_mobile = phone_mobile
        self.phone_home = phone_home
        self.email = email

def populate():
    session = DBSession()
    session.flush()
    transaction.commit()
    
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        DBSession.rollback()
