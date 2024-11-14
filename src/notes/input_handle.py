from colorama import Fore
from src.decorators.input_error import input_error
from src.notes.classes.notebook import Notebook
from src.notes.classes.note import Note

# Function add note with data in args (title, note) to the dict notebook
@input_error
def add_note(notebook: Notebook):
    title = input("Please enter title of note: ").strip().lower()
    content = input("Please enter content of note: ").strip()
    add_tag = input("Do you wanna add tags? (yes/no): ").strip().lower()
    if (add_tag == "yes"):
        tags = input("Please enter tags for note: ").strip().split()
    else:
        tags = []
    
    note = notebook.find_by_title(title)

    if note is None:
        if tags == []: 
            note = Note(title, content)
        else:
            formated_tags = {*tags}
            note = Note(title, content, list(formated_tags))
        notebook.add_note(note)
        return f"{Fore.GREEN}Note added.{Fore.RESET}"
    else:
        raise ValueError(f"{Fore.YELLOW}Note with this title is already exist{Fore.RESET}")
    

# Function add tags to note to the dict notebook  
@input_error
def add_tags_to_note(notebook: Notebook):
    title = input("Please enter title of note: ").strip().lower()
    tags = input("Please enter tags splited by space: ").strip().split()

    if tags == []:
        return f"{Fore.YELLOW}No tags was printed{Fore.RESET}"

    note: Note = notebook.find_by_title(title)

    if note is not None:
        formated_tags = {*tags}
        note.add_tags(list(formated_tags))
        return f"{Fore.GREEN}Tags for note added.{Fore.RESET}"
    else:
        raise ValueError(f"{Fore.YELLOW}Note with this title is not exist{Fore.RESET}")


# Function to find notes by tag
@input_error
def find_note_by_tag(args: list[str], notebook: Notebook):
    try:
        tag, *_ = args
    except ValueError:
        return f"{Fore.YELLOW}Please enter tag by which you want to find notes{Fore.RESET}"
    
    return notebook.find_by_tag(tag)


# Function for editing notes
@input_error
def edit_note(notebook: Notebook):
    title = input("Please enter title of note: ").strip().lower()
    content = input("Please enter new content of note: ").strip()
    
    note: Note = notebook.find_by_title(title)

    if note is not None:
        note.update_content(content)
        return f"{Fore.GREEN}Note content updated.{Fore.RESET}"
    else:
        raise ValueError(f"{Fore.YELLOW}Note with this title is not exist{Fore.RESET}")


# Function for deleting notes
@input_error
def delete_note(args: list[str], notebook: Notebook):
    try:
        title, *_ = args
    except ValueError:
        return f"{Fore.YELLOW}Please enter title of note that you want to delete{Fore.RESET}"
    
    note: Note = notebook.find_by_title(title.lower())

    if note is not None:
        notebook.delete_note(title.lower())
        return f"{Fore.GREEN}Note deleted.{Fore.RESET}"
    else:
        raise ValueError(f"{Fore.YELLOW}Note with this title is not exist{Fore.RESET}")


# Function takes dict of notes and return it, if no notes return 'No notes found'
@input_error
def show_all_notes(notebook: Notebook) -> str:
    if len(notebook) == 0:
        return f'{Fore.YELLOW}No notes found{Fore.RESET}'
    
    return notebook   