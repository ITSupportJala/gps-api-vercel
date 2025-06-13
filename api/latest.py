from http.server import BaseHTTPRequestHandler
import json

from api.push_data import latest_data  # share variabel

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(latest_data).encode())
