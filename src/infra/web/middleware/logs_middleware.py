from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from datetime import datetime
import logging

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.now()
        response = await call_next(request)
        process_time = (datetime.now() - start_time).total_seconds()

        logger = logging.getLogger("webserver_logger")
        log_record = {
            "method": request.method,
            "url": request.url.path,
            "remoteAddr": request.client.host,
            "processTime": process_time,
            "status_code": response.status_code,
            "message": response.body.decode("utf-8")
        }
        logger.info(log_record)
        

        return response
    
    