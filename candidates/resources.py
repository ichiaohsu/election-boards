import falcon

from candidates.models import Candidate, CandidateTerms

class CandidateResource(object):
    
    def on_get(self, req, resp):
        pass
class CandidateTermResource(object):

    def on_get(self, req, resp):
        pass

candidates = CandidateResource()
cadidates_terms = CandidateTermResource()