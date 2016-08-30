from sqlalchemy import (
    Column,
    Index,
    Integer,
    UnicodeText,
    Date
)

from .meta import Base


class MyEntry(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    body = Column(UnicodeText)
    creation_date = Column(Date)


# Index('my_index', MyEntry.title, unique=True, mysql_length=255)
