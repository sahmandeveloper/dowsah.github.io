from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def run():
    httpd = HTTPServer(('127.0.0.1', 80), MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
