def main():
    """
        --- Day 7: No Space Left On Device ---

    You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

    The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

    $ system-update --please --pretty-please-with-sugar-on-top
    Error: No space left on device

    Perhaps you can delete some files to make space for the update?

    You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k

    The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

    Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

        cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
            cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
            cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
            cd / switches the current directory to the outermost directory, /.
        ls means list. It prints out all of the files and directories immediately contained by the current directory:
            123 abc means that the current directory contains a file named abc with size 123.
            dir xyz means that the current directory contains a directory named xyz.

    Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

    - / (dir)
      - a (dir)
        - e (dir)
          - i (file, size=584)
        - f (file, size=29116)
        - g (file, size=2557)
        - h.lst (file, size=62596)
      - b.txt (file, size=14848514)
      - c.dat (file, size=8504156)
      - d (dir)
        - j (file, size=4060174)
        - d.log (file, size=8033020)
        - d.ext (file, size=5626152)
        - k (file, size=7214296)

    Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

    Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

    The total sizes of the directories above can be found as follows:

        The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
        The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
        Directory d has total size 24933642.
        As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.

    To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

    Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

    Your puzzle answer was 2031851.
    --- Part Two ---

    Now, you're ready to choose a directory to delete.

    The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

    In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

    To achieve this, you have the following options:

        Delete directory e, which would increase unused space by 584.
        Delete directory a, which would increase unused space by 94853.
        Delete directory d, which would increase unused space by 24933642.
        Delete directory /, which would increase unused space by 48381165.

    Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
    """
    with open('files.txt', 'r') as terminal_input:
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
    directory_file_sizes = get_directory_file_sizes(home, {})
    sum_of_sub_100000_files = 0
    for value in directory_file_sizes.values():
        if value <= 100000:
            sum_of_sub_100000_files += value
    print(f'The sum of all files under 100000 size is {sum_of_sub_100000_files}')
    print(f'The sum of all files is {home.file_size}')
    free_space = 70000000 - home.file_size
    space_to_free_up = 30000000 - free_space
    print(f'Therefore we must find a directory with size at least {space_to_free_up}')
    all_sizes = list(directory_file_sizes.values())
    file_to_delete = min(all_sizes, key=lambda x:abs(x - space_to_free_up))
    print(f'You should delete the file with size: {file_to_delete}')


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

def get_directory_file_sizes(directory, directory_file_sizes):
    if directory.directories:
        for new_directory in directory.directories:
            directory_file_sizes = get_directory_file_sizes(new_directory, directory_file_sizes)
    directory_file_sizes[directory.name + directory.parent.name if directory.parent else "no parent"] = directory.file_size
    return directory_file_sizes


class Directory(object):
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.directories = []
        self.parent = None

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    @property
    def file_size(self):
        total_file_size = 0
        if not self.directories:
            file_size = sum(self.files.values())
            return sum(self.files.values())
        else:
            for directory in self.directories:
                total_file_size += directory.file_size
            return total_file_size + sum(self.files.values())

    def add_directories(self, directory):
        self.directories.append(directory)

    def add_file(self, file):
        size, name = file.split(' ')
        self.files[name] = int(size)

    def add_parent(self, directory):
        self.parent = directory


if __name__ == "__main__":
    main()