from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class http_server(BaseHTTPRequestHandler):
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send message back to client
        with open('webpages/simple.html') as fin:
            for line in fin:
                self.wfile.write(bytes(line, "utf8"))
        return

def run():
  print('starting server...')
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access, so its a no go y'all
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, http_server)
  print('running server...')
  httpd.serve_forever()
run()
