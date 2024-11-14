from prompt_toolkit.completion import Completer, Completion
from src.constants import COMMANDS

# Completer for prompt_toolkit that matches commands.
class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text.lower()
        matches = [cmd for cmd in COMMANDS.values() if cmd.startswith(text)]
        for match in matches:
            yield Completion(match, start_position=-len(text))
