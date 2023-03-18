from app.database import Base
from sqlalchemy import String,  Integer, Column, Text, Date


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(Text)
    published_date = Column(Date)
   
