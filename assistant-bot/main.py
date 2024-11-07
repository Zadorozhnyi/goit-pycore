from src.contacts.models.address_book import AddressBook
from src.notes.models.notebook import Notebook
from src.utils.parse_input import parse_input
from src.contacts.input_handle import *
from src.notes.input_handle import *

# Bot version
def get_app_version():
    return "1.0.0"

def main():

    # Load existing address book data if available
    address_book = AddressBook.load_data()

    # Load existing Notebook data if available
    notebook = Notebook.load_notebook()
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Save data before exiting
            address_book.save_data()
            notebook.save_notebook()
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(address_book))
        elif command == "change":
            print(change_contact(args, address_book))
        elif command == "contact-by-name":
            print(find_contact_by_name(args, address_book))
        elif command == "contact-by-phone":
            print(find_contact_by_phone(args, address_book))
        elif command == "delete-phone":
            print(delete_phone(args, address_book))
        elif command == "phone":
            print(show_phone(args, address_book))
        elif command == "all-contacts":
            print(show_all_contacts(address_book))
        elif command == "add-birthday":
            print(add_birthday(args, address_book))
        elif command == "show-birthday":
            print(show_birthday(args, address_book))
        elif command == "birthdays":
            print(birthdays(address_book))
        elif command == "birthdays-in-days":
            print(birthdays_in_days(args, address_book))
        elif command == "add-note":
            print(add_note(notebook))
        elif command == "add-tags":
            print(add_tags_to_note(notebook))
        elif command == "find-note":
            print(find_note_by_tag(args, notebook))
        elif command == "edit-note":
            print(edit_note(notebook))
        elif command == "delete-note":
            print(delete_note(args, notebook))
        elif command == "all-notes":
            print(show_all_notes(notebook))
        elif command == "version":
            print(get_app_version())
        else:
            print("Sorry, buy this command is invalid!")


# Start the main function
if __name__ == "__main__":
    main()
