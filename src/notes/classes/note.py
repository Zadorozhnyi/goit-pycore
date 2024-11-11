from colorama import Fore

# Class Note for support: tags, search, and editing
class Note:
    def __init__(self, title: str, content: str, tags=[]):
        self.title = title
        self.content = content
        self.tags = tags

    # Add tags to the note by taking tags
    def add_tags(self, tags):
        self.tags.extend(tags)
        self.tags = list({*self.tags})

    # Edit note from the notebook by taking new content,
    def update_content(self, new_content):
        self.content = new_content

    def __str__(self):
        tags = "No tags for now" if self.tags == [] else ", ".join(self.tags)
        return f'\n{Fore.GREEN}Note title:{Fore.RESET} {self.title.capitalize()}\nContent: {self.content}\nTags: {tags}\n'