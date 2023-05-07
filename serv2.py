from http.server import BaseHTTPRequestHandler
import http.server
import socketserver

PORT = 8000

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/doc'
        try:
          f = open(self.path[1:]).read() 
          self.send_response(200)
          self.end_headers()
          self.wfile.write(bytes(f, 'utf-8'))

        except:
            f = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(f, 'utf-8'))
        
with socketserver.TCPServer(("", PORT), Serv) as httpd:
    print(f"Ready {PORT}")
    httpd.serve_forever()
