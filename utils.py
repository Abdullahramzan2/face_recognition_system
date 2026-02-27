import logging
import os
from config import LOG_PATH

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Create logger
logger = logging.getLogger("face_recognition_system")
logger.setLevel(logging.DEBUG)

# File handler — logs everything to file
file_handler = logging.FileHandler(LOG_PATH)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Console handler — only shows warnings and above
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
console_handler.setFormatter(console_formatter)

# Attach handlers (avoid duplicate handlers on reload)
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def log_info(message: str):
    """Log an informational message to the log file."""
    logger.info(message)


def log_warning(message: str):
    """Log a warning to the log file and console."""
    logger.warning(message)


def log_error(message: str):
    """Log an error to the log file and console."""
    logger.error(message)