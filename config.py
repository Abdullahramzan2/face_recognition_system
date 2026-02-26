import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "faces")
LOG_PATH = os.path.join(BASE_DIR, "logs", "app.log")

MODEL_NAME = "Facenet"
DETECTOR_BACKEND = "opencv"
DISTANCE_THRESHOLD = 0.6