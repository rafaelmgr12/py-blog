import logging
import json
from datetime import datetime



class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "filename": record.filename,
            "lineno": record.lineno,
            "funcName": record.funcName
        }
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_record)