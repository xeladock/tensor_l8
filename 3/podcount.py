#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from requests import get
from re import findall as reget

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, endpoint='/metrics'):
  server_address = ('',8100)
  httpd = server_class(server_address, handler_class, endpoint)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()
class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        res = get('http://10.78.84.3:8080/api/v1/pods')
        s = str(res.content)
        pods = (int(len(reget('containers', s)) / 2))
        itog = 'total_pods_count '+ str(pods)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f'{itog}'.encode())

run(handler_class=HttpGetHandler)
