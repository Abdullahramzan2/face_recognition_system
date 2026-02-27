from register import register_user
from recognize import recognize_faces
from utils import log_info


def main():
    print("Face Recognition System")

    while True:
        print("\n1. Register User")
        print("2. Start Recognition")
        print("3. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            if not username:
                print("[!] Username cannot be empty.")
                continue
            register_user(username)

        elif choice == "2":
            recognize_faces()

        elif choice == "3":
            print("Goodbye!")
            log_info("Application exited by user.")
            break

        else:
            print("[!] Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()