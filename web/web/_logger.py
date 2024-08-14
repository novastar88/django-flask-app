import os
import sys
from loguru import logger
from django.conf import settings


_file = {"sink": os.path.join(os.path.join(settings.BASE_DIR, "log"), "{time:DD_MM_YYYY}.log"), "level": "TRACE",
         "rotation": "25 MB", "retention": "1 day", "enqueue": True, "format":
             "<level>{level}</level> | <green>{time:DD.MM.YYYY HH:mm:ss}</green> | <cyan>{function}</cyan> - <magenta>{message}</magenta> | {extra}"}
_console = {"sink": sys.stderr, "colorize": True, "level": "TRACE", "format":
            "<level>{level}</level> | <green>{time:DD.MM.YYYY HH:mm:ss}</green> | <cyan>{file}:{function}</cyan> - <magenta>{message}</magenta>"}

logger.configure(handlers=[_file, _console])
