from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MockHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/login':
            # 读取请求的数据
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            # 模拟验证账号密码
            if data.get('email') == 'eve.holt@reqres.in' and data.get('password') == 'cityslicka':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"token": "QpwL5tke4Pnpja7X4"}).encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Missing password"}).encode())

if __name__ == '__main__':
    print("Mock 服务已启动，监听 127.0.0.1:8000")
    server = HTTPServer(('127.0.0.1', 8000), MockHandler)
    server.serve_forever()