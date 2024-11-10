from colorama import Fore

# Decorator for error handling
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{Fore.YELLOW}This contact does not exist{Fore.RESET}"
        except ValueError as err:
            return err.args[0]
        except IndexError:
            return f"{Fore.YELLOW}Enter the argument for the command{Fore.RESET}"
    return inner