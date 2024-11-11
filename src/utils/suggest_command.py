from colorama import Fore
import difflib
from src.constants import COMMANDS

def suggest_command(user_input):
    closest_match = difflib.get_close_matches(user_input, COMMANDS.values(), n=1)
    return f"{Fore.YELLOW}Did you mean: '{closest_match[0]}'?{Fore.YELLOW}"  if closest_match else ""