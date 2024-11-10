from colorama import Fore
from src.constants import COMMANDS

def show_menu():
    description_common = {
        COMMANDS["HELP"]: "Show menu of bot",
        COMMANDS["HELLO"]: "Say hello to the bot",
        COMMANDS["CLOSE"]: "Exit from program",
        COMMANDS["EXIT"]: "Exit from program",
        COMMANDS["SHOW_VERSION"]: "Show version of bot",
    }

    description_contacts = {
        COMMANDS["ADD_CONTACT"]: {
            "arg": "",
            "desc": "Add a new contact"
        },
        COMMANDS["CHANGE_PHONE_OF_CONTACT"]: {
            "arg": "    |name|  |old_phone|  |new_phone|",
            "desc": "Change the phone number"
        },
        COMMANDS["FIND_CONTACT_BY_NAME"]: {
            "arg": "    |name|",
            "desc": "Find contact by name"
        },
        COMMANDS["FIND_CONTACT_BY_PHONE"]: {
            "arg": "    |phone|",
            "desc": "Find contact by phone"
        },
        COMMANDS["DELETE_PHONE"]: {
            "arg": "    |name|  |phone|",
            "desc": "Delete phone from the contact"
        },
        COMMANDS["DELETE_CONTACT"]: {
            "arg": "    |name|",
            "desc": "Delete contact"
        },
        COMMANDS["SHOW_PHONE"]: {
            "arg": "    |name|",
            "desc": "Show phones of the contact"
        },
        COMMANDS["ALL_CONTACTS"]: {
            "arg": "",
            "desc": "Show all contacts"
        },
        COMMANDS["ADD_BIRTHDAY"]: {
            "arg": "    |name|  |birthday|",
            "desc": "Add birthday to the contact"
        },
        COMMANDS["SHOW_BIRTHDAY"]: {
            "arg": "    |name|",
            "desc": "Show birthday of the contact"
        },
        COMMANDS["GET_UPCOMING_BIRTHDAYS"]: {
            "arg": "",
            "desc": "Get contacts with upcoming birthdays"
        },
        COMMANDS["GET_BIRTHDAYS_IN_DAYS"]: {
            "arg": "    |days|",
            "desc": "Get contacts with birthdays in <opt> days"
        },
    }

    description_notes = {
        COMMANDS["ADD_NOTE"]: {
            "arg": "",
            "desc": "Add a new contact"
        },
        COMMANDS["ADD_TAGS"]: {
            "arg": "",
            "desc": "Add tags to the note"
        },
        COMMANDS["FIND_NOTE_BY_TAG"]: {
            "arg": "  |tag|",
            "desc": "Find note by tag"
        },
        COMMANDS["EDIT_NOTE_CONTENT"]: {
            "arg": "",
            "desc": "Edit content of note"
        },
        COMMANDS["DELETE_NOTE"]: {
            "arg": "  |title|",
            "desc": "Delete note"
        },
        COMMANDS["ALL_NOTES"]: {
            "arg": "",
            "desc": "Show all notes"
        },
    }

    rows_common = []
    for key, value in description_common.items():
        rows_common.append(f'{Fore.BLUE}|{Fore.RESET}{key:<15}{Fore.BLUE}|{Fore.RESET}{value:<25}{Fore.BLUE}|{Fore.RESET}\n')
    table_common = f'\n{" "*17}Common{" "*17}\n{Fore.BLUE}{"-"*42}\n|{Fore.RESET}{" "*4}Command{" "*4}{Fore.BLUE}|{Fore.RESET}{" "*7}Description{" "*7}{Fore.BLUE}|{Fore.RESET}\n{Fore.BLUE}{"-"*42}{Fore.RESET}\n{"".join(rows_common)}{Fore.BLUE}{"-"*42}{Fore.RESET}\n'

    rows_contacts = []
    for key, value in description_contacts.items():
        rows_contacts.append(f'{Fore.BLUE}|{Fore.RESET}{key:<20}{Fore.BLUE}|{Fore.RESET}{value["arg"]:<42}{Fore.BLUE}|{Fore.RESET}{value["desc"]:<45}{Fore.BLUE}|{Fore.RESET}\n')
    table_contacts = f'\n{" "*49}Contacts{" "*49}\n{Fore.BLUE}{"-"*110}\n|{Fore.RESET}{" "*6}Command{" "*7}{Fore.BLUE}|{Fore.RESET}{" "*16}Arguments{" "*17}{Fore.BLUE}|{Fore.RESET}{" "*17}Description{" "*17}{Fore.BLUE}|\n{"-"*110}{Fore.RESET}\n{"".join(rows_contacts)}{Fore.BLUE}{"-"*110}{Fore.RESET}\n'

    rows_notes = []
    for key, value in description_notes.items():
        rows_notes.append(f'{Fore.BLUE}|{Fore.RESET}{key:<15}{Fore.BLUE}|{Fore.RESET}{value["arg"]:<15}{Fore.BLUE}|{Fore.RESET}{value["desc"]:<25}{Fore.BLUE}|\n')
    table_notes = f'\n{" "*25}Notes{" "*25}\n{Fore.BLUE}{"-"*58}\n|{Fore.RESET}{" "*4}Command{" "*4}{Fore.BLUE}|{Fore.RESET}{" "*3}Arguments{" "*3}{Fore.BLUE}|{Fore.RESET}{" "*7}Description{" "*7}{Fore.BLUE}|{Fore.RESET}\n{Fore.BLUE}{"-"*58}{Fore.RESET}\n{"".join(rows_notes)}{Fore.BLUE}{"-"*58}{Fore.RESET}\n'

    return f"{table_common}\n{table_contacts}\n{table_notes}"