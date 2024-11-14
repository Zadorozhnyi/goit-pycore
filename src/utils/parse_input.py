from prompt_toolkit import PromptSession
from src.utils.classes.command_completer import CommandCompleter
from src.decorators.input_error import input_error

# CLI Functions
@input_error
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def get_prompt_pession():
    return PromptSession(completer=CommandCompleter(), multiline=False)