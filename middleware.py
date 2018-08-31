from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    'postgresql://127.0.0.1:5432/election_boards'
)

class SQLAlchemySessionManager(object):
    """
    Create a scoped session for every request and close it when the request
    ends.
    """

    def __init__(self):
        session_factory = sessionmaker(bind=engine)
        self.Session = scoped_session(session_factory)

    def process_resource(self, req, resp, resource, params):
        resource.session = self.Session

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            if not req_succeeded:
                resource.session.rollback()
            self.Session.close()