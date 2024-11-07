import re
from src.utils.classes.field import Field

# Class for store and validate e-mail
class Email(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if not re.fullmatch(r'^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,63}\.[a-zA-Z]{2,10}$', value):
            raise ValueError("Invalid email format.")