"""A console contact book using a dictionary."""


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def add_or_update(contacts):
    name = read_non_empty("Name: ")
    phone = read_non_empty("Phone: ")
    email = input("Email (optional): ").strip()
    contacts[name.casefold()] = {
        "name": name,
        "phone": phone,
        "email": email,
    }
    print("Contact saved.")


def search_contact(contacts):
    query = input("Enter a name to search: ").strip().casefold()
    contact = contacts.get(query)
    if contact is None:
        print("Contact not found.")
        return

    print(f"Name:  {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email'] or '(not provided)'}")


def list_contacts(contacts):
    if not contacts:
        print("Your contact book is empty.")
        return

    print("\n--- Contacts ---")
    for key in sorted(contacts):
        contact = contacts[key]
        print(f"{contact['name']} — {contact['phone']}")


def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip().casefold()
    if contacts.pop(name, None) is None:
        print("Contact not found.")
    else:
        print("Contact deleted.")


def main():
    contacts = {}

    while True:
        print("\n===== Contact Book =====")
        print("1. Add or update contact")
        print("2. Search contact")
        print("3. List contacts")
        print("4. Delete contact")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_or_update(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            list_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3, 4, or 0.")


if __name__ == "__main__":
    main()
