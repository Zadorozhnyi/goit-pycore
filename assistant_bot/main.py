import pickle
import re
from collections import UserDict
from datetime import datetime, timedelta

# Base class Field
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


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
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if not re.fullmatch(r'^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,63}\.[a-zA-Z]{2,10}$', value):
            raise ValueError("Invalid email format.")


# Class for store addresses
class Address(Field):
    pass


# Decorator for error handling
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist"
        except ValueError as err:
            return err.args[0]
        except IndexError:
            return "Enter the argument for the command"
    return inner


# Function for store data to file
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


# Function for restore data from the file
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Return a new address book if the file is not found
        return AddressBook()


# Function for store Notebook to file
def save_notebook(notebook, filename="notebook.pkl"):
    pass


# Function for restore Notebook from the file
def load_notebook(filename="notebook.pkl"):
    pass


# Class for storing and validation birthday
class Birthday(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(self.value)

    def validate(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'DD.MM.YYYY'.")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


# Class to store name
class Name(Field):
    pass


# Class for storing and validation phone number
class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must contain exactly 10 digits.")

    def validate(self, value):
        return value.isdigit() and len(value) == 10


# Class for storing records
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    # Add phone to the record by taking phone, if phone is already exist return
    def add_phone(self, phone_number:str):
        if str(Phone(phone_number)) in self.phones:
            raise ValueError('Phone is already exist.')
        self.phones.append(str(Phone(phone_number)))
        return self.phones

    # Remove phone from the record by taking phone, if phone not exist return
    def remove_phone(self, phone_number: str):
        if str(Phone(phone_number)) not in self.phones:
            raise ValueError('Phone is not in phones')
        self.phones.remove(phone_number)

    # Edit phone from the record by taking phone and new phone
    def edit_phone(self, old_phone_number: str, new_phone_number:str):
        # Check if phone exist
        self.find_phone(old_phone_number)

        phone_index = self.phones.index(old_phone_number)
        self.phones.remove(old_phone_number)
        self.phones.insert(phone_index, new_phone_number)

    # Find phone from the record by taking phone
    def find_phone(self, phone_number: str):
        if str(Phone(phone_number)) not in self.phones:
            raise KeyError
        return phone_number

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_adress(self, new_address):
        self.address = Address(new_address)

    def add_email(self, new_email):
        self.email = Email(new_email)

    def __str__(self):
        phones_str = '\n  phones: ' + ', '.join(p.value for p in self.phones) if self.phones else ''
        birthday_str = f"\n  birthday: {self.birthday}" if self.birthday else ""
        address_str = f"\n  address: {self.address}" if self.address else ""
        email_str = f"\n  email: {self.email}" if self.email else ""
        return f"Contact name: {self.name.value}{phones_str}{address_str}{email_str}{birthday_str}"


# Class for work with address book
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return
        return 'No records with this name'

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        upcoming_week = today + timedelta(days=7)
        result = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value
                birthday_this_year = birthday.replace(year=today.year)

                # If the birthday already passed this year, check next year
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                # Check if birthday is within the next 7 days
                if today <= birthday_this_year <= upcoming_week:
                    # If birthday falls on a weekend, postpone to next Monday
                    if birthday_this_year.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
                        birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

                    result.append({
                        'name': record.name.value,
                        'birthday': birthday_this_year.strftime("%d.%m.%Y")
                    })

        return result


# CLI Functions
@input_error
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(address_book: AddressBook):
    name = input('Enter name: ').strip()
    if not name:
        raise ValueError("Name cannot be empty. Please try again.")

    record = address_book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        address_book.add_record(record)
        message = "Contact added."

    try:
        phone = input('Enter phone: ').strip()
        if phone:
            record.add_phone(phone)

        address = input('Enter address: ').strip()
        if address:
            record.add_adress(address)

        email = input('Enter email: ').strip()
        if email:
            record.add_email(email)

        birthday = input('Enter birthday (DD.MM.YYYY): ').strip()
        if birthday:
            record.add_birthday(birthday)

    except ValueError as e:
        if message == "Contact added.":
            address_book.delete(name)
        return f"{e} Please try again."

    return message


@input_error
def change_contact(args, address_book: AddressBook):
    # Function takes data about contact and update phone of contact by name
    try:
        name, phone, new_phone, *_ = args
    except ValueError:
        return 'Please enter name, old phone and new phone!'
    
    record: Record = address_book.find(name)
    if record:
        record.edit_phone(phone, new_phone)
        return f"Contact '{name}' updated."
    raise KeyError

@input_error
def delete_phone(args, address_book: AddressBook):
    # Function takes data about contact and delete phone of contact by name
    try:
        name, phone, *_ = args
    except ValueError:
        return 'Please enter name of contact and phone that want to delete!'
    
    record: Record = address_book.find(name)
    if record:
        record.remove_phone(phone)
        return f"Contact '{name}' updated."
    raise KeyError

@input_error
def show_phone(args, address_book: AddressBook):
    name = args[0]
    record = address_book.find(name)
    if record:
        return f"Phone for '{name}': {', '.join([p.value for p in record.phones])}"
    raise KeyError


@input_error
def add_birthday(args, address_book: AddressBook):
    name, birthday = args
    record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday for '{name}' added/updated."
    raise KeyError


@input_error
def show_birthday(args, address_book: AddressBook):
    name = args[0]
    record = address_book.find(name)
    if record and record.birthday:
        return f"Birthday for '{name}': {record.birthday}"
    raise KeyError


@input_error
def birthdays(address_book: AddressBook):
    upcoming_birthdays = address_book.get_upcoming_birthdays()
    if upcoming_birthdays:
        result = "\n".join([f"{contact['name']} - {contact['birthday']}" for contact in upcoming_birthdays])
        return f"Upcoming birthdays:\n{result}"
    return "No upcoming birthdays in the next 7 days."


@input_error
def birthdays_in_days(args, address_book: AddressBook):
    try:
        days = int(args[0])
        today = datetime.now().date()
        upcoming_date = today + timedelta(days=days)
        result = []
        for record in address_book.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                # Перевіряємо, чи день народження в межах заданої кількості днів
                if today <= birthday_this_year <= upcoming_date:
                    result.append(f"{record.name.value} - {birthday_this_year.strftime('%d.%m.%Y')}")
        if result:
            return "Birthdays in the next {} days:\n{}".format(days, "\n".join(result))
        return f"No birthdays in the next {days} days."
    except ValueError:
        return "Please specify the number of days as an integer."



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
def show_all_contacts(book: AddressBook):
    if book.data.items():
        return ('\n'*2).join(str(record) for record in book.data.values())
    return 'The address book is empty.'


def suggest_command(user_input):
    pass


def main():
    # Load existing address book data if available
    address_book = load_data()

    # Load existing Notebook data if available
    notebook = load_notebook()
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Save data before exiting
            save_data(address_book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(address_book))
        elif command == "change":
            print(change_contact(args, address_book))
        elif command == "delete-phone":
            print(delete_phone(args, address_book))
        elif command == "phone":
            print(show_phone(args, address_book))
        elif command == "all":
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
