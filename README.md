# Python Programming: Foundations and Best Practices. Final project

Personal assistant for managing contacts and notes

## Description

We can add contact by name, phone, email, birthday.

We can change all info about contact.

We can delete phone.

We can see how many friends have upcoming birthdays.

We can add notes and tags and change them.

We can find notes by tags.

We can delete notes if no more need them.


## Getting Started

### Dependencies

* List the dependencies present in the local ``pyproject.toml`` file:
```
python = "^3.8"
prompt-toolkit = "^3.0.48"
colorama = "^0.4.6"
```

## Installation

Follow the steps below to install and set up the project:

### Prerequisites

Before installing, ensure you have the following dependencies installed:
- [Python ^3.8](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [pipx](https://pipx.pypa.io/stable/)

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zadorozhnyi/goit-pycore.git
   ```

2. **Install the application**:
* For Windows, run:
   ```
    install-win.bat
   ```

* For Linux or MAC run:
   ```
    install-unix.sh
   ```

2. **Uninstall the application**:
* For Windows, run:
   ```
    uninstall-win.bat
   ```

* For Linux or MAC run:
   ```
    uninstall-unix.sh
   ```

### Executing assistant-bot

* To run the application:

   ```
    assistant-bot <help or path to store data>
   ```

## Help

```
                 Common
------------------------------------------ 
|    Command    |       Description       |
------------------------------------------ 
|help           |Show menu of bot         |
|hello          |Say hello to the bot     |
|close          |Exit from program        |
|exit           |Exit from program        |
|version        |Show version of bot      |
------------------------------------------


                                                 Contacts
--------------------------------------------------------------------------------------------------------------
|      Command       |                Arguments                 |                 Description                 |
--------------------------------------------------------------------------------------------------------------
|add                 |                                          |Add a new contact                            |
|change              |    |name|  |old_phone|  |new_phone|      |Change the phone number                      |
|contact-by-name     |    |name|                                |Find contact by name                         |
|contact-by-phone    |    |phone|                               |Find contact by phone                        |
|delete-phone        |    |name|  |phone|                       |Delete phone from the contact                |
|phone               |    |name|                                |Show phones of the contact                   |
|all-contacts        |                                          |Show all contacts                            |
|add-birthday        |    |name|  |birthday|                    |Add birthday to the contact                  |
|show-birthday       |    |name|                                |Show birthday of the contact                 |
|birthdays           |                                          |Get contacts with upcoming birthdays         |
|birthdays-in-days   |    |days|                                |Get contacts with birthdays in <opt> days    |
--------------------------------------------------------------------------------------------------------------


                         Notes
----------------------------------------------------------
|    Command    |   Arguments   |       Description       |
----------------------------------------------------------
|add-note       |               |Add a new contact        |
|add-tags       |               |Add tags to the note     |
|find-note      |  |tag|        |Find note by tag         |
|edit-note      |               |Edit content of note     |
|delete-note    |  |title|      |Delete note              |
|all-notes      |               |Show all notes           |
----------------------------------------------------------
```

## Authors

2024 CleverPath team

## Version History

* 1.0.0
    * Initial Release
* 1.1.0
    * Various bug fixes and optimizations
* 1.2.0
    * Final Release

## License
MIT, see ``license.txt``