from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)
    level = Column(String, default="A1")
    score = Column(Integer, default=0)

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.tg_id"))
    lesson_id = Column(Integer)
    status = Column(String)
