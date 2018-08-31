import falcon

from middleware import SQLAlchemySessionManager
from boards import BoardResource
from wsgiref import simple_server

app = falcon.API(middleware=[
    SQLAlchemySessionManager(),
])

boards = BoardResource()
app.add_route('/boards/{bid:int}', boards)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()