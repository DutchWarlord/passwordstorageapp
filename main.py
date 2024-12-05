from passwordfunctions import *


def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password)
            print(f"Password for {service} added successfully.")
        
        elif choice == '2':
            service = input("Enter the service name: ")
            password = retrieve_password(service)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print(f"No password found for {service}.")
        
        elif choice == '3':
            service = input("Enter the service name: ")
            new_password = input("Enter the new password: ")
            update_password(service, new_password)
            print(f"Password for {service} updated successfully.")
        
        elif choice == '4':
            service = input("Enter the service name: ")
            delete_password(service)
            print(f"Password for {service} deleted successfully.")
        
        elif choice == '5':
            print("Exiting Password Manager.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()