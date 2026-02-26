import cv2
from deepface import DeepFace
from config import DB_PATH, MODEL_NAME, DETECTOR_BACKEND, DISTANCE_THRESHOLD
from utils import log_info, log_error

def recognize_faces():
    try:
        cap = cv2.VideoCapture(0)

        print("Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            label = "Unknown"
            confidence_text = ""

            try:
                result = DeepFace.find(
                    img_path=frame,
                    db_path=DB_PATH,
                    model_name=MODEL_NAME,
                    detector_backend=DETECTOR_BACKEND,
                    enforce_detection=False
                )

                if len(result) > 0 and len(result[0]) > 0:

                    best_match = result[0].iloc[0]
                    distance = best_match["distance"]

                    if distance <= DISTANCE_THRESHOLD:
                        identity = best_match["identity"]
                        label = identity.split("\\")[-2]
                        confidence = round((1 - distance) * 100, 2)
                        confidence_text = f"{confidence}%"
                    else:
                        label = "Unknown"

            except Exception as e:
                log_error(str(e))

            # Display result
            display_text = f"{label} {confidence_text}"
            cv2.putText(frame, display_text,
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0) if label != "Unknown" else (0, 0, 255),
                        2)

            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        log_info("Recognition session ended.")

    except Exception as e:
        log_error(str(e))
        print("Error:", e)