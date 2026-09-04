# -*- coding: utf-8 -*-
"""
Local preview server for the TWJ site.

    python _tools/serve.py [port]      (run from Baldy/web)

Plain `python -m http.server` dies with a ConnectionResetError when a browser
drops a connection mid-response — which Chrome does routinely while scrubbing
through a page. This wrapper swallows those, serves from the site root no
matter where it is started from, and disables caching so a rebuild always
shows up on refresh.
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8123


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            self.close_connection = True

    def log_message(self, fmt, *args):
        if not str(args[0] if args else "").startswith("GET /assets"):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    os.chdir(ROOT)
    print("serving %s at http://127.0.0.1:%d/" % (ROOT, PORT))
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
