from register import register_user
from recognize import recognize_faces

def main():
    print("1. Register User")
    print("2. Start Recognition")

    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter username: ")
        register_user(username)

    elif choice == "2":
        recognize_faces()

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()