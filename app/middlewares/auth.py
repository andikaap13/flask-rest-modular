from werkzeug.wrappers import Request, Response, ResponseStream

import jwt

class Auth():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        if 'x-access-token' in request.headers:
            token = request.headers['X-Access-Token']
        
        res = Response('Authorization Failed!', mimetype= 'text/plain', status=401)
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            return self.app(environ, start_response)
        except:
            return res(environ, start_response)