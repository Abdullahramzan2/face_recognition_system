import cv2 # type: ignore
import os
from deepface import DeepFace # type: ignore
from config import (
    DB_PATH, MODEL_NAME, DETECTOR_BACKEND, DISTANCE_THRESHOLD,
    FONT, FONT_SCALE, FONT_THICKNESS,
    COLOR_KNOWN, COLOR_UNKNOWN,
    BOX_COLOR_KNOWN, BOX_COLOR_UNKNOWN
)
from utils import log_info, log_error


def get_username_from_path(identity_path: str) -> str:
    """Extract username from identity path in a cross-platform way."""
    # Normalize path separators for Windows and Linux/Mac
    parts = identity_path.replace("\\", "/").split("/")

    if len(parts) >= 2:
        return parts[-2]
    return "Unknown"


def draw_face_box(frame, facial_area: dict, label: str, confidence_text: str, is_known: bool):
    """Draw a bounding box and label around a detected face."""
    box_color = BOX_COLOR_KNOWN if is_known else BOX_COLOR_UNKNOWN
    text_color = COLOR_KNOWN if is_known else COLOR_UNKNOWN
    

    x = facial_area.get("x", 0)
    y = facial_area.get("y", 0)
    w = facial_area.get("w", 0)
    h = facial_area.get("h", 0)

    # Draw rectangle
    cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

    # Draw label background
    display_text = f"{label} {confidence_text}".strip()
    (text_w, text_h), baseline = cv2.getTextSize(display_text, FONT, FONT_SCALE, FONT_THICKNESS)
    cv2.rectangle(frame, (x, y - text_h - baseline - 6), (x + text_w, y), box_color, -1)

    # Draw label text
    cv2.putText(
        frame,
        display_text,
        (x, y - baseline - 4),
        FONT,
        FONT_SCALE,
        (255, 255, 255),
        FONT_THICKNESS
    )

    return frame


def recognize_faces():
    """Start real-time face recognition using webcam."""
    if not os.path.exists(DB_PATH) or not os.listdir(DB_PATH):
        print("[!] No registered users found. Please register at least one user first.")
        log_error("Recognition attempted with empty database.")
        return

    try:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("[!] Could not open camera.")
            log_error("Camera not accessible during recognition.")
            return

        print("[*] Press 'q' to quit recognition.")
        log_info("Recognition session started.")

        while True:
            ret, frame = cap.read()
            if not ret:
                log_error("Failed to read frame from camera.")
                break

            label = "Unknown"
            confidence_text = ""
            is_known = False
            facial_area = {}

            try:
                results = DeepFace.find(
                    img_path=frame,
                    db_path=DB_PATH,
                    model_name=MODEL_NAME,
                    detector_backend=DETECTOR_BACKEND,
                    enforce_detection=False,
                    silent=True
                )

                if results and len(results[0]) > 0:
                    best_match = results[0].iloc[0]
                    distance = best_match.get("distance", 1.0)

                    if distance <= DISTANCE_THRESHOLD:
                        identity = best_match.get("identity", "")
                        label = get_username_from_path(identity)
                        confidence = round((1 - distance) * 100, 2)
                        confidence_text = f"{confidence}%"
                        is_known = True

                    # Try to get facial area for bounding box
                    for col in ["source_x", "source_y", "source_w", "source_h"]:
                        pass
                    facial_area = {
                        "x": int(best_match.get("source_x", 50)),
                        "y": int(best_match.get("source_y", 50)),
                        "w": int(best_match.get("source_w", 150)),
                        "h": int(best_match.get("source_h", 150)),
                    }

            except Exception as e:
                log_error(f"Recognition error: {str(e)}")

            # Draw bounding box and label if we have facial area info
            if facial_area:
                frame = draw_face_box(frame, facial_area, label, confidence_text, is_known)
            else:
                # Fallback: simple text overlay
                display_text = f"{label} {confidence_text}".strip()
                color = COLOR_KNOWN if is_known else COLOR_UNKNOWN
                cv2.putText(frame, display_text, (50, 50), FONT, FONT_SCALE, color, FONT_THICKNESS)

            cv2.imshow("Face Recognition - Press Q to quit", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        log_info("Recognition session ended.")
        print("[*] Recognition stopped.")

    except Exception as e:
        log_error(f"Critical recognition error: {str(e)}")
        print(f"[!] Error: {e}")