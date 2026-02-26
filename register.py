import cv2
import os
from config import DB_PATH
from utils import log_info, log_error

def register_user(username):
    try:
        os.makedirs(DB_PATH, exist_ok=True)

        user_path = os.path.join(DB_PATH, username)
        os.makedirs(user_path, exist_ok=True)

        cap = cv2.VideoCapture(0)

        print("Press 's' to save face, 'q' to quit.")

        count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                log_error("Camera not accessible")
                break

            cv2.imshow("Register Face", frame)

            key = cv2.waitKey(1)

            if key == ord('s'):
                img_path = os.path.join(user_path, f"{count}.jpg")
                cv2.imwrite(img_path, frame)
                print(f"Saved {img_path}")
                count += 1

            elif key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        log_info(f"User {username} registered successfully.")

    except Exception as e:
        log_error(str(e))
        print("Error:", e)