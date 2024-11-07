from src.contacts.classes.fields.name import Name
from src.contacts.classes.fields.phone import Phone
from src.contacts.classes.fields.birthday import Birthday
from src.contacts.classes.fields.address import Address
from src.contacts.classes.fields.email import Email

# Class for storing records
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    # Add phone to the record by taking phone, if phone is already exist return
    def add_phone(self, phone_number: str):
        if str(Phone(phone_number)) in [str(phone) for phone in self.phones]:
            raise ValueError('Phone is already exist.')
        self.phones.append(Phone(phone_number))
        return self.phones

    # Remove phone from the record by taking phone, if phone not exist return
    def remove_phone(self, phone_number: str):
        if str(Phone(phone_number)) not in [str(phone) for phone in self.phones]:
            raise ValueError('Phone is not in phones')
        phone_index = [str(phone) for phone in self.phones].index(phone_number)
        del self.phones[phone_index]

    # Edit phone from the record by taking phone and new phone
    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        # Check if phone exist
        self.find_phone(old_phone_number)

        phone_index = [str(phone) for phone in self.phones].index(old_phone_number)
        del self.phones[phone_index]
        self.phones.insert(phone_index, Phone(new_phone_number))

    # Find phone from the record by taking phone
    def find_phone(self, phone_number: str):
        if str(Phone(phone_number)) not in [str(phone) for phone in self.phones]:
            raise KeyError
        return phone_number

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_adress(self, new_address):
        self.address = Address(new_address)

    def add_email(self, new_email):
        self.email = Email(new_email)

    def __str__(self):
        phones_str = '\nphones: ' + ', '.join(p.value for p in self.phones) if self.phones else ''
        birthday_str = f"\nbirthday: {self.birthday}" if self.birthday else ""
        address_str = f"\naddress: {self.address}" if self.address else ""
        email_str = f"\nemail: {self.email}" if self.email else ""
        return f"\nContact name: {self.name.value}{phones_str}{address_str}{email_str}{birthday_str}\n"