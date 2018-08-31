import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship

Model = declarative_base()

class Boards(Model):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    # contributor_id = Column(UUID, ForeignKey('contributors.id'))
    # contibuted_by = relationship('Contributors', backref='boards')

    def __init__(self, created_at):
        self.created_at = created_at

    def __json__(self):
        return ['song', 'src', 'type', 'created_at']
# class Contributors(base):
#     __tablename__ = 'contributors'

#     id = Column(UUID, primary_key=True)
