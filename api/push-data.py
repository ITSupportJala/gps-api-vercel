from http.server import BaseHTTPRequestHandler
import json

latest_data = {}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        global latest_data
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        data = json.loads(body)

        # Simpan ke memori global
        latest_data = data

        # (Opsional) Relay ke lokal kamu jika pakai ngrok
        # import requests
        # requests.post("http://localhost:5000/gps/receive", json=data)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success"}).encode())
