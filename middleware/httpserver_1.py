from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys
import json
import logging

#hoverctl middleware --remote http://localhost:8080/HoverflyHttpMW/helloServlet
#hoverctl middleware --remote http://localhost:9090/
#hoverctl import Simulation05Jun1600.json
#hoverctl mode simulate
#http://localhost:8888/api/v2/hoverfly

logging.basicConfig(filename='middleware_http.log', level=logging.DEBUG)
logging.debug('Middleware "middleware_http" called')

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print self.path
        print parse_qs(self.path[2:])
        self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        payload_dict = json.loads(post_data)
        logging.debug(post_data)
        if "response" in payload_dict and "body" in payload_dict["response"]:
           payload_dict["response"]["body"] = "{\"Name\": \"Madan\", \"Job\": \"Leader\"}"		
        self._set_headers()
        logging.debug(json.dumps(payload_dict))
        self.wfile.write(json.dumps(payload_dict))

def run(server_class=HTTPServer, handler_class=GP, port=9090):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:9090...'
    httpd.serve_forever()

run()