from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_DIRECTORY = Path(__file__).resolve().parent


class ProjectRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIRECTORY), **kwargs)


def main() -> None:
    address = ("127.0.0.1", 8000)
    server = ThreadingHTTPServer(address, ProjectRequestHandler)
    print(f"RE.CIRCULA disponível em http://{address[0]}:{address[1]}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()