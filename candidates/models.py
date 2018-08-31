from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Model = declarative_base()

class Candidate(Model):
    __tablename__ = 'candidates'

class CandidateTerms(Model):
    __tablename__ = 'candidates_terms'

    uid = Column('uid', String(70), unique=True)
    type = Column('type', String(20))

