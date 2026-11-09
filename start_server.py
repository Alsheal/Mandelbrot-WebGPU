from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "localhost"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Сервер запущен: http://{HOST}:{PORT}")
print("Для остановки нажмите Ctrl+C")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен")
    server.server_close()