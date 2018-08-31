import falcon

from middleware import SQLAlchemySessionManager
from boards.resources import boards
from candidates.resources import candidates, cadidates_terms
from wsgiref import simple_server

app = falcon.API(middleware=[
    SQLAlchemySessionManager(),
])

# app.add_route('/boards', boards)
app.add_route('/candidates', candidates)
app.add_route('/candidates_terms', candidates_terms)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8080, app)
    httpd.serve_forever()