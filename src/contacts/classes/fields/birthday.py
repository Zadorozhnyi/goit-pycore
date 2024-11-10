from colorama import Fore
from datetime import datetime
from src.utils.classes.field import Field

# Class for storing and validation birthday
class Birthday(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(self.value)

    def validate(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(f"{Fore.YELLOW}Invalid date format. Use 'DD.MM.YYYY'.{Fore.RESET}")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")