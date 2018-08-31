import falcon
import json
from boards.models import Board
from datetime import datetime, timedelta

class BoardResource(object):
    
    def on_get(self, req, resp):
        
        # if bid is None:
        #     print("bid is None")
        # boards = self.session.query(Boards).all()
        # resp.status = falcon.HTTP_200
        # resp.body = json.dumps({'_items': boards})
        pass   
    def on_post(self, req, resp):

        b = Board(datetime.utcnow() - timedelta(hours=3))
        self.session.add(b)
        self.session.commit()

boards = BoardResource()
