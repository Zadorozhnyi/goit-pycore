from datetime import datetime, timedelta
from colorama import Fore
from src.decorators.input_error import input_error
from src.contacts.classes.address_book import AddressBook
from src.contacts.classes.record import Record
from src.contacts.classes.fields.phone import Phone


@input_error
def add_contact(address_book: AddressBook):
    name = input('Enter name: ').strip()
    if not name:
        raise ValueError(f"{Fore.YELLOW}Name cannot be empty. Please try again.{Fore.RESET}")

    record = address_book.find(name)
    message = f"{Fore.GREEN}Contact updated.{Fore.RESET}"

    if record is None:
        record = Record(name)
        address_book.add_record(record)
        message = f"{Fore.GREEN}Contact added.{Fore.RESET}"

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
        if message == f"{Fore.GREEN}Contact added.{Fore.RESET}":
            address_book.delete(name)
        return f"{Fore.YELLOW}{e} {Fore.YELLOW}Please try again.{Fore.RESET}"

    return message


@input_error
def find_contact_by_name(args, address_book: AddressBook):
    try:
        name, *_ = args
    except ValueError:
        return f'{Fore.YELLOW}Please enter contact name near the command!{Fore.RESET}'

    record = address_book.find(name)
    if record:
        return str(record)
    raise ValueError(f"{Fore.YELLOW}Contact with name '{name}' not found.{Fore.RESET}")


@input_error
def find_contact_by_phone(args, address_book: AddressBook):
    try:
        phone, *_ = args
    except ValueError:
        return f'{Fore.YELLOW}Please enter phone number near the command!{Fore.RESET}'

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
    raise ValueError(f"{Fore.YELLOW}Contact with phone number '{phone}' not found.{Fore.RESET}")


@input_error
def change_contact(args, address_book: AddressBook):
    # Function takes data about contact and update phone of contact by name
    try:
        name, phone, new_phone, *_ = args
    except ValueError:
        return f'{Fore.YELLOW}Please enter name, old phone and new phone near the command!{Fore.RESET}'
    
    record: Record = address_book.find(name)
    if record:
        record.edit_phone(phone, new_phone)
        return f"{Fore.GREEN}Contact '{name}' updated.{Fore.RESET}"
    raise KeyError


@input_error
def delete_phone(args, address_book: AddressBook):
    # Function takes data about contact and delete phone of contact by name
    try:
        name, phone, *_ = args
    except ValueError:
        return f'{Fore.YELLOW}Please enter name of contact and phone that want to delete!{Fore.RESET}'
    
    record: Record = address_book.find(name)
    if record:
        record.remove_phone(phone)
        return f"{Fore.GREEN}Contact '{name}' updated.{Fore.RESET}"
    raise KeyError


@input_error
def delete_contact(args, address_book: AddressBook):
    # Function takes data about contact and delete contact
    try:
        name, *_ = args
    except ValueError:
        return f"{Fore.YELLOW}Please enter name of contact that you want to delete{Fore.RESET}"
    
    record: Record = address_book.find(name)

    if record is not None:
        address_book.delete(name)
        return f"{Fore.GREEN}Contact deleted.{Fore.RESET}"
    else:
        raise ValueError(f"{Fore.YELLOW}Contact with this name is not exist{Fore.RESET}")
    

@input_error
def show_phone(args, address_book: AddressBook):
    try:
        name = args[0]
    except IndexError:
        return f'{Fore.YELLOW}Please enter name of contact near the command!{Fore.RESET}'

    record = address_book.find(name)
    if record:
        return f"Phone for '{name}': {', '.join([p.value for p in record.phones])}"
    raise KeyError


@input_error
def add_birthday(args, address_book: AddressBook):
    try:
        name, birthday, *_ = args
    except ValueError:
        return f'{Fore.YELLOW}Please enter name of contact and birthday near the command!{Fore.RESET}'
    
    record: Record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"{Fore.GREEN}Birthday for '{name}' added/updated.{Fore.RESET}"
    raise KeyError


@input_error
def show_birthday(args, address_book: AddressBook):
    try:
        name = args[0]
    except IndexError:
        return f'{Fore.YELLOW}Please enter name of contact near the command!{Fore.RESET}'
    
    record: Record = address_book.find(name)
    if record and record.birthday:
        return f"Birthday for '{name}': {record.birthday}"
    raise ValueError(f'{Fore.YELLOW}Contact has not info about birthday{Fore.RESET}')


@input_error
def birthdays(address_book: AddressBook):
    upcoming_birthdays = address_book.get_upcoming_birthdays()
    if upcoming_birthdays:
        result = "\n".join([f"{contact['name']} - {contact['birthday']}" for contact in upcoming_birthdays])
        return f"\n{Fore.GREEN}Upcoming birthdays:{Fore.RESET}\n{result}\n"
    return f"{Fore.YELLOW}No upcoming birthdays in the next 7 days.{Fore.RESET}"


@input_error
def birthdays_in_days(args, address_book: AddressBook):
    try:
        try:
            days = int(args[0])
        except IndexError:
            return f'{Fore.YELLOW}Please enter number of days near the command!{Fore.RESET}'
        
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
            return "\n{}Birthdays in the next {} days:{}\n{}\n".format(Fore.GREEN, days, Fore.RESET, "\n".join(result))
        return f"{Fore.YELLOW}No birthdays in the next {days} days.{Fore.RESET}"
    except ValueError:
        return f"{Fore.YELLOW}Please specify the number of days as an integer.{Fore.RESET}"


@input_error
def show_all_contacts(book: AddressBook):
    if book.data.items():
        return ('\n'*2).join(str(record) for record in book.data.values())
    return f'{Fore.YELLOW}The address book is empty.{Fore.RESET}'