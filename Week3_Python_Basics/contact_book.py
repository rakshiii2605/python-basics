def add_contact(name, number):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{number}\n")
    print(f"Contact {name} saved successfully.")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            else:
                print("\nSaved Contacts:")
                for contact in contacts:
                    name, number = contact.strip().split(",")
                    print(f"Name: {name} | Number: {number}")
    except FileNotFoundError:
        print("No contacts file found. Please add a contact first.")

# Demo usage
print("Simple Contact Book")
print("1. Add Contact")
print("2. View Contacts")
choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter name: ")
    number = input("Enter number: ")
    add_contact(name, number)
elif choice == "2":
    view_contacts()
else:
    print("Invalid choice.")
