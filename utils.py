import logging
from config import LOG_PATH
import os

# Create logs directory if not exists
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)