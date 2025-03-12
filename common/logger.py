import logging

from core.config import settings


class ColoredFormatter(logging.Formatter):
    LOG_COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
        "RESET": "\033[0m",  # Reset color
    }

    def format(self, record):
        log_color = self.LOG_COLORS.get(record.levelname, None)
        log_message = super().format(record)

        if log_color:
            reset = self.LOG_COLORS["RESET"]
            return f"{log_color}{log_message}{reset}"

        return log_message


class Logger:
    """
    Log messages to the console

    Example: [2025-01-01 12:45:59] [<function_name>] [INFO] This is an info message
    """

    def __init__(self, name="aicore_logger"):
        self.name = name
        # Log level ("DEBUG", "INFO" etc)
        log_level_str = settings.LOGGING_LEVEL
        # Parse log level
        self.level = getattr(logging, log_level_str)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.level)

        # Prevent adding duplicate handlers
        if not self.logger.hasHandlers():
            # Add handlers to logger
            self.logger.addHandler(self._console_handler())

        # Prevent custom logger messages from propagating to the root logger
        # to avoid duplicates and conflicts with other loggers
        self.logger.propagate = False

    def _console_handler(self):
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)

        formatter = ColoredFormatter(
            "[%(asctime)s] [%(funcName)s] [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)
        return console_handler


logger = Logger().logger
