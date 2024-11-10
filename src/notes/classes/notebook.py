from colorama import Fore
import pickle
from collections import UserDict
from src.notes.classes.note import Note
from pathlib import Path

# Class Notebook for storing and managing notes
class Notebook(UserDict):
    # Add note to the dict by taking note
    def add_note(self, note: Note):
        self.data[str(note.title)] = note
    
     # Find note in dict by taking title
    def find_by_title(self, title: str):
        if title in self.data:
            return self.data[title]
        return None

    def find_by_tag(self, tag):
        notes = '\n'.join([str(note) for note in self.data.values() if tag in note.tags])
        if notes == "":
            return f"{Fore.YELLOW}No notes with this tag found{Fore.RESET}"
        else:
            return notes

    # Function that delete note in dict by taking title
    def delete_note(self, title: str):
        if title in self.data:
            del self.data[title]
            return
        return f'{Fore.YELLOW}No notes with this title{Fore.RESET}'

    # Function for restore Notebook from the file
    @classmethod
    def load_notebook(cls, path, filename="notebook.pkl"):
        try:
            with open(Path(path) / filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return cls()

    # Function for store Notebook to file
    def save_notebook(self, path, filename="notebook.pkl"):
        with open(Path(path) / filename, 'wb') as file:
            pickle.dump(self, file)

    def __str__(self):
        return '\n'.join([str(note) for note in self.data.values()])