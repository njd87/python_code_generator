# class that generates code in a new language from python
# calls ocaml file for abstraction

class Code_Writer():
    def __init__(self, directory=""):
        self.directory = directory
        self.commands = []

    def generate(self, name="new_file", ext=".jl"):
        with open(name + ext) as file:
            for command in self.commands:
                file.write(translate_command(command, ext))

def translate_command(command):
    pass