from http.server import BaseHTTPRequestHandler, HTTPServer

name= "0.0.0.0"
port = 8000


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>HTTP Python Server.</h1>", "utf-8"))
        self.wfile.write(bytes("<p>Aleks Dzhartov. This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":       
    
    webServer = HTTPServer((name, port), MyServer)
    webServer.serve_forever()
    
