import falcon
import json
from models import Boards
from datetime import datetime, timedelta

class BoardResource(object):
    
    def on_get(self, req, resp, bid):
        
        if bid is None:
            print("bid is None")
        boards = self.session.query(Boards).all()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'_items': boards})

    def on_post(self, req, resp, bid):

        b = Boards(datetime.utcnow() - timedelta(hours=3))
        self.session.add(b)
        self.session.commit()