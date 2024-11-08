from src.contacts.classes.address_book import AddressBook
from src.notes.classes.notebook import Notebook
from src.utils.parse_input import parse_input, get_prompt_pession
from src.utils.show_menu import show_menu
from src.utils.suggest_command import suggest_command
from src.contacts.input_handle import *
from src.notes.input_handle import *
from src.constants import COMMANDS

# Bot version
def get_app_version():
    return "1.1.0"

def main():

    # Load existing address book data if available
    address_book = AddressBook.load_data()

    # Load existing Notebook data if available
    notebook = Notebook.load_notebook()

    session = get_prompt_pession()

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = session.prompt("Enter a command: ").strip()
            command, *args = parse_input(user_input)
        except (EOFError, KeyboardInterrupt):
            command = "close"

        if command in [COMMANDS["CLOSE"], COMMANDS["EXIT"]]:
            # Save data before exiting
            address_book.save_data()
            notebook.save_notebook()
            print("Good bye!")
            break
        elif command == COMMANDS["HELP"]:
            print(show_menu())
        elif command == COMMANDS["HELLO"]:
            print("How can I help you?")
        elif command == COMMANDS["ADD_CONTACT"]:
            print(add_contact(address_book))
        elif command == COMMANDS["CHANGE_PHONE_OF_CONTACT"]:
            print(change_contact(args, address_book))
        elif command == COMMANDS["FIND_CONTACT_BY_NAME"]:
            print(find_contact_by_name(args, address_book))
        elif command == COMMANDS["FIND_CONTACT_BY_PHONE"]:
            print(find_contact_by_phone(args, address_book))
        elif command == COMMANDS["DELETE_PHONE"]:
            print(delete_phone(args, address_book))
        elif command == COMMANDS["SHOW_PHONE"]:
            print(show_phone(args, address_book))
        elif command == COMMANDS["ALL_CONTACTS"]:
            print(show_all_contacts(address_book))
        elif command == COMMANDS["ADD_BIRTHDAY"]:
            print(add_birthday(args, address_book))
        elif command == COMMANDS["SHOW_BIRTHDAY"]:
            print(show_birthday(args, address_book))
        elif command == COMMANDS["GET_UPCOMING_BIRTHDAYS"]:
            print(birthdays(address_book))
        elif command == COMMANDS["GET_BIRTHDAYS_IN_DAYS"]:
            print(birthdays_in_days(args, address_book))
        elif command == COMMANDS["ADD_NOTE"]:
            print(add_note(notebook))
        elif command == COMMANDS["ADD_TAGS"]:
            print(add_tags_to_note(notebook))
        elif command == COMMANDS["FIND_NOTE_BY_TAG"]:
            print(find_note_by_tag(args, notebook))
        elif command == COMMANDS["EDIT_NOTE_CONTENT"]:
            print(edit_note(notebook))
        elif command == COMMANDS["DELETE_NOTE"]:
            print(delete_note(args, notebook))
        elif command == COMMANDS["ALL_NOTES"]:
            print(show_all_notes(notebook))
        elif command == COMMANDS["SHOW_VERSION"]:
            print(get_app_version())
        else:
            print(f"Unknown command. {suggest_command(command)}")


# Start the main function
if __name__ == "__main__":
    main()