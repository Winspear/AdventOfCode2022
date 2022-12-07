import gc

class Directory(object):
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.file_size = self.files.values()
        self.directories = []
        self.parent = None

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def add_directories(self, directory):
        self.directories.append(directory)

    def add_file(self, file):
        size, name = file.split(' ')
        self.files[name] = size

    def add_parent(self, directory):
        self.parent = directory

def main():
    with open('files_test.txt', 'r') as terminal_input:
        lines = [line.rstrip() for line in terminal_input if line.rstrip() != '$ ls']
        home = Directory('/')
        current_directory = home
        lines_to_parse = []
        for line in lines:
            if "$ cd" in line:
                process_current_directory(current_directory, lines_to_parse)
                lines_to_parse = []
                current_directory = choose_new_current_directory(current_directory, line)
            else:
                lines_to_parse.append(line)
        process_current_directory(current_directory, lines_to_parse)
        size_of_all_files_in_directories = get_directory_sizes()
    print(current_directory.files)

def process_current_directory(current_directory, lines_to_parse):
    for line in lines_to_parse:
        if "dir " in line:
            folder_chars, name = line.split(" ")
            new_directory = Directory(name)
            new_directory.add_parent(current_directory)
            current_directory.add_directories(new_directory)
        else:
            current_directory.add_file(line)

def choose_new_current_directory(current_directory, line):
    if line == '$ cd ..':
        return current_directory.parent
    elif line == '$ cd /':
        return current_directory
    else:
        bash, cd, name = line.split(" ")
        for directory in current_directory.directories:
            if directory.name == name:
                return directory
        raise Exception(f'Couldn\t find any child directories with name {name}')


if __name__ == "__main__":
    main()