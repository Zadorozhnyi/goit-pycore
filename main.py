from collections import UserDict

# Base class Field
class Field:
    def __init__(self, value):
        pass

    def __str__(self):
        pass


# Class Note for support: tags, search, and editing
class Note:
    def __init__(self, content, tags=None):
        pass

    def add_tag(self, tag):
        pass

    def update_content(self, new_content):
        pass

    def __str__(self):
        pass


# Class Notebook for storing and managing notes
class Notebook:
    def __init__(self):
        pass

    def add_note(self, content, tags=None):
        pass

    def find_by_tag(self, tag):
        pass

    def edit_note_content(self, note_index, new_content):
        pass

    def delete_note_by_index(self, note_index):
        pass

    def __str__(self):
        pass


# Class for store and validate e-mail
class Email(Field):
    def __init__(self, value):
        pass

    def validate(self):
        pass


# Class for store addresses
class Address(Field):
    pass


# Decorator for error handling
def input_error(func):
    def inner(*args, **kwargs):
        pass
    return inner


# Function for store data to file
def save_data(book, filename="addressbook.pkl"):
    pass


# Function for restore data from the file
def load_data(filename="addressbook.pkl"):
    pass


# Function for store Notebook to file
def save_notebook(notebook, filename="notebook.pkl"):
    pass


# Function for restore Notebook from the file
def load_notebook(filename="notebook.pkl"):
    pass


# Class for storing and validation birthday
class Birthday(Field):
    def __init__(self, value):
        pass

    def validate(self):
        pass

    def __str__(self):
        pass


# Class to store name
class Name(Field):
    pass


# Class for storing and validation phone number
class Phone(Field):
    def __init__(self, value):
        pass

    def validate(self):
        pass


# Class for storing records
class Record:
    def __init__(self, name):
        pass

    def add_email(self, email):
        pass

    def add_address(self, address):
        pass

    def add_phone(self, phone_number):
        pass

    def remove_phone(self, phone_number):
        pass

    def edit_phone(self, old_phone_number, new_phone_number):
        pass

    def find_phone(self, phone_number):
        pass

    def add_birthday(self, birthday):
        pass

    def __str__(self):
        pass


# Class for work with address book
class AddressBook(UserDict):
    def add_record(self, record):
        pass

    def find(self, name):
        pass

    def delete(self, name):
        pass

    def get_upcoming_birthdays(self):
        pass

    def get_birthdays_in_days(self, days):
        pass


# CLI Functions
@input_error
def parse_input(user_input):
    pass


@input_error
def add_contact(args, address_book: AddressBook):
    pass


@input_error
def change_contact(args, address_book: AddressBook):
    pass


@input_error
def show_phone(args, address_book: AddressBook):
    pass


@input_error
def add_birthday(args, address_book: AddressBook):
    pass


@input_error
def show_birthday(args, address_book: AddressBook):
    pass


@input_error
def birthdays(address_book: AddressBook):
    pass


@input_error
def birthdays_in_days(args, address_book: AddressBook):
    pass


@input_error
def add_note(args, notebook: Notebook):
    pass


@input_error
def find_note_by_tag(args, notebook: Notebook):
    pass


# Function for editing notes
@input_error
def edit_note(args, notebook: Notebook):
    pass


# Function for deleting notes
@input_error
def delete_note(args, notebook: Notebook):
    pass


@input_error
def show_all(address_book: AddressBook):
    pass


def suggest_command(user_input):
    pass


def main():
    # Load existing address book data if available
    address_book = load_data()

    # Load existing Notebook data if available
    notebook = load_notebook()
    # notebook = Notebook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Save data before exiting
            pass
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, address_book))
        elif command == "change":
            print(change_contact(args, address_book))
        elif command == "phone":
            print(show_phone(args, address_book))
        elif command == "all":
            print(show_all(address_book))
        elif command == "add-birthday":
            print(add_birthday(args, address_book))
        elif command == "show-birthday":
            print(show_birthday(args, address_book))
        elif command == "birthdays":
            print(birthdays(address_book))
        elif command == "birthdays-in-days":
            print(birthdays_in_days(args, address_book))
        elif command == "add-note":
            print(add_note(args, notebook))
        elif command == "find-note":
            print(find_note_by_tag(args, notebook))
        elif command == "edit-note":
            print(edit_note(args, notebook))
        elif command == "delete-note":
            print(delete_note(args, notebook))
        else:
            print(suggest_command(command))


# Start the main function
if __name__ == "__main__":
    main()
