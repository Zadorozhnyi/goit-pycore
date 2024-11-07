from src.utils.models.field import Field

# Class for storing and validation phone number
class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must contain exactly 10 digits.")

    def validate(self, value):
        return value.isdigit() and len(value) == 10