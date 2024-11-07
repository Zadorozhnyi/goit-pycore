from datetime import datetime, timedelta
from src.decorators.input_error import input_error
from src.contacts.models.address_book import AddressBook
from src.contacts.models.record import Record
from src.contacts.models.fields.phone import Phone

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
def find_contact_by_name(args, address_book: AddressBook):
    try:
        name, *_ = args
    except ValueError:
        return 'Please enter contact name near the command!'

    record = address_book.find(name)
    if record:
        return str(record)
    raise ValueError(f"Contact with name '{name}' not found.")


@input_error
def find_contact_by_phone(args, address_book: AddressBook):
    try:
        phone, *_ = args
    except ValueError:
        return 'Please enter phone number near the command!'

    valid_phone = Phone(phone)
    records = []
    for record in address_book.data.values():
        try:
            if record.find_phone(str(valid_phone)):
                records.append(record)
        except KeyError:
            continue
    if records:
        return ('\n'*2).join(str(record) for record in records)
    raise ValueError(f"Contact with phone number '{phone}' not found.")


@input_error
def change_contact(args, address_book: AddressBook):
    # Function takes data about contact and update phone of contact by name
    try:
        name, phone, new_phone, *_ = args
    except ValueError:
        return 'Please enter name, old phone and new phone near the command!'
    
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
    try:
        name = args[0]
    except IndexError:
        return 'Please enter name of contact near the command!'

    record = address_book.find(name)
    if record:
        return f"Phone for '{name}': {', '.join([p.value for p in record.phones])}"
    raise KeyError


@input_error
def add_birthday(args, address_book: AddressBook):
    try:
        name, birthday, *_ = args
    except ValueError:
        return 'Please enter name of contact and birthday near the command!'
    
    record: Record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday for '{name}' added/updated."
    raise KeyError


@input_error
def show_birthday(args, address_book: AddressBook):
    try:
        name = args[0]
    except IndexError:
        return 'Please enter name of contact near the command!'
    
    record: Record = address_book.find(name)
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
        try:
            days = int(args[0])
        except IndexError:
            return 'Please enter number of days near the command!'
        
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
def show_all_contacts(book: AddressBook):
    if book.data.items():
        return ('\n'*2).join(str(record) for record in book.data.values())
    return 'The address book is empty.'