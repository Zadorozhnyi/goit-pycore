from colorama import Fore
from src.utils.classes.field import Field

# Class for storing and validation phone number
class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError(f"{Fore.YELLOW}Phone number must contain exactly 10 digits.{Fore.RESET}")

    def validate(self, value):
        return value.isdigit() and len(value) == 10