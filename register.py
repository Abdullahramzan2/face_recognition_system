import cv2 # type: ignore
import os
from config import DB_PATH, MAX_PHOTOS_PER_USER, FONT, FONT_SCALE, FONT_THICKNESS
from utils import log_info, log_error


def register_user(username: str):
    """Register a new user by capturing face images from the webcam."""
    try:
        # Sanitize username to prevent path issues
        username = username.strip().replace(" ", "_")
        if not username:
            print("[!] Invalid username.")
            return

        os.makedirs(DB_PATH, exist_ok=True)
        user_path = os.path.join(DB_PATH, username)

        # Check if user already exists
        if os.path.exists(user_path) and os.listdir(user_path):
            print(f"[!] User '{username}' already has registered faces.")
            overwrite = input("   Overwrite existing data? (y/n): ").strip().lower()
            if overwrite != "y":
                print("[*] Registration cancelled.")
                return

        os.makedirs(user_path, exist_ok=True)

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("[!] Could not open camera.")
            log_error("Camera not accessible during registration.")
            return

        print(f"\n[*] Registering user: '{username}'")
        print(f"[*] Press 'S' to save a photo ({MAX_PHOTOS_PER_USER} max), 'Q' to finish.\n")

        count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                log_error("Failed to read frame from camera during registration.")
                break

            # Overlay instructions and count on the frame
            display_frame = frame.copy()
            info_text = f"Saved: {count}/{MAX_PHOTOS_PER_USER} | S=Save  Q=Quit"
            cv2.putText(display_frame, info_text, (10, 30), FONT, 0.7, (255, 255, 0), 2)

            # Draw a center guide rectangle to help user frame their face
            h, w = display_frame.shape[:2]
            cx, cy = w // 2, h // 2
            box_size = 180
            cv2.rectangle(
                display_frame,
                (cx - box_size, cy - box_size),
                (cx + box_size, cy + box_size),
                (255, 255, 0), 2
            )
            cv2.putText(display_frame, "Align face here", (cx - box_size, cy - box_size - 10),
                        FONT, 0.6, (255, 255, 0), 2)

            cv2.imshow(f"Register: {username} - Press Q to quit", display_frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('s') or key == ord('S'):
                if count >= MAX_PHOTOS_PER_USER:
                    print(f"[!] Max photos ({MAX_PHOTOS_PER_USER}) reached. Press 'Q' to finish.")
                else:
                    img_path = os.path.join(user_path, f"{count}.jpg")
                    cv2.imwrite(img_path, frame)
                    count += 1
                    print(f"[+] Photo {count}/{MAX_PHOTOS_PER_USER} saved.")

                    if count >= MAX_PHOTOS_PER_USER:
                        print(f"[*] Maximum photos reached. Press 'Q' to finish registration.")

            elif key == ord('q') or key == ord('Q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        if count > 0:
            log_info(f"User '{username}' registered with {count} photo(s).")
            print(f"\n[✓] User '{username}' registered successfully with {count} photo(s).")
        else:
            # Clean up empty folder
            os.rmdir(user_path)
            print(f"[!] No photos saved. Registration cancelled for '{username}'.")
            log_info(f"Registration cancelled for '{username}' — no photos captured.")

    except Exception as e:
        log_error(f"Registration error: {str(e)}")
        print(f"[!] Error during registration: {e}")