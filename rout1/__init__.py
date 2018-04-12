from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
routing_table = {}

def route(url, func):
routing_table[url] = func

def find_path(url):
if url in routing_table:
    return routing_table[url]
else:
    return None

def app(environ, start_response):
setup_testing_defaults(environ)
handler = find_path(environ['PATH_INFO'])
if handler is None:
    status = '404 Not Found'
    body = "<html><body><h1>Page Not Found</h1></body></html>"
else:
    status = '200 OK'
    body = handler()
headers = [('Content-type', 'text/html: charset=utf-8')]
start_response(status, headers)
return [body.encode("utf-8")]

def run(ip, port):
myserver = make_server(ip, port, app)
print("Serving testings of wsgi at http://%s:%s" % (ip, port))
myserver.serve_forever()