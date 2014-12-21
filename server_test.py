#import BaseHTTPServer
#import SimpleHTTPServer
#import SocketServer
#
#PORT = 8000
#
#
#class TestRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
#    def do_GET(self):
#        self.send_response(200)
#        self.send_header("Content-Length", "TEST TEST")
#        self.end_headers()
#
#
#handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#
#httpd = SocketServer.TCPServer(("", PORT), handler)
#
#print "serving at port", PORT
#httpd.serve_forever()
from time import sleep

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    sleep(1)
    return 'test answer!'

if __name__ == '__main__':
    app.run()