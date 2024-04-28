import json
import logging
import uvicorn
from typing import Callable, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infra.web.middleware.logs_middleware import LoggingMiddleware
from src.infra.web.utils.json_formatter import JsonFormatter

# Setup logging with JSON output
logger = logging.getLogger("webserver_logger")
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs.json', mode='a')
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)





class WebServer:
    def __init__(self, port: int, host: str = 'localhost'):
        self.app = FastAPI()
        self.port = port
        self.host = host
        self.configure_middlewares()
        self.health_check_route()

    def configure_middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["https://*", "http://*"],
            allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            allow_headers=["Accept", "Authorization",
                           "Content-Type", "X-CSRF-Token"],
            expose_headers=["Link"],
        )
        self.app.add_middleware(LoggingMiddleware)

    def health_check_route(self):
        @self.app.get("/api/healthchecker")
        async def root():
            return {"message": "Welcome to FastAPI"}

    def add_route(self, path: str, endpoint: Callable, methods: List[str]):
        for method in methods:
            if method.upper() == "GET":
                self.app.get(path)(endpoint)
            elif method.upper() == "POST":
                self.app.post(path)(endpoint)
            elif method.upper() == "PUT":
                self.app.put(path)(endpoint)
            elif method.upper() == "PATCH":
                self.app.put(path)(endpoint)
            elif method.upper() == "DELETE":
                self.app.delete(path)(endpoint)

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
