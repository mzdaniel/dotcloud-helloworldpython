'''WSGI web interface exercising hello function'''

from helloworld.application import hello

def application(environ, start_response):
    '''Standard boilerplate wsgi code'''
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [hello()]

