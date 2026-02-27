import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "faces")
LOG_PATH = os.path.join(BASE_DIR, "logs", "app.log")

# DeepFace model settings
MODEL_NAME = "Facenet"          # Options: Facenet, VGG-Face, ArcFace, Dlib, etc.
DETECTOR_BACKEND = "opencv"     # Options: opencv, ssd, mtcnn, retinaface
DISTANCE_THRESHOLD = 0.6        # Lower = stricter matching

# Registration settings
MAX_PHOTOS_PER_USER = 10        # Max number of face images saved per user

# Display settings
FONT = 0                        # cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.9
FONT_THICKNESS = 2
COLOR_KNOWN = (0, 255, 0)       # Green for known faces
COLOR_UNKNOWN = (0, 0, 255)     # Red for unknown faces
BOX_COLOR_KNOWN = (0, 255, 0)
BOX_COLOR_UNKNOWN = (0, 0, 255)