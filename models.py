from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'community_movie_list'
    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    image_url = Column(String)
    updated = Column(Date)
    url_streaming = Column(String)

