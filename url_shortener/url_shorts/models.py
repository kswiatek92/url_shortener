from sqlalchemy import Column, Integer, String, Text

from url_shortener.database import Base


class URLShorts(Base):
    __tablename__ = "url_shorts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(Text, unique=True, nullable=False)
    shortened_url = Column(String(128), unique=True, nullable=False)

    def __init__(self, original_url, shortened_url, *args, **kwargs):
        self.original_url = original_url
        self.shortened_url = shortened_url
