from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from datetime import datetime
import logging


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        start_time = datetime.now()
        response = await call_next(request)
        process_time = (datetime.now() - start_time).total_seconds()

        body = b""
        async for chunk in response.body_iterator:
            body += chunk

        new_response = Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
        )

        logger = logging.getLogger("webserver_logger")
        log_record = {
            "method": request.method,
            "url": request.url.path,
            "remoteAddr": request.client.host,
            "processTime": process_time,
            "status_code": response.status_code,
            "response": body.decode(),  #
        }
        logger.info(log_record)

        return new_response
