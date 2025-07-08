#!/usr/bin/env python3
"""
Simple web server to serve our congratulations page!
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"🎉 Congratulations server running at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
