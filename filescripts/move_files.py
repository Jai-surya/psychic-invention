import sys
from datetime import *
import shutil
import os
import os.path

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
source_path = ''
destination_path = ''
drop_count = 0


def check_arg():
    if len(sys.argv) != 3:
        print('Script Use Case :'
              '\n<py> <move_files.py> <source_path> <destination_path>')
        exit()
    else:
        global source_path, destination_path
        source_path = sys.argv[1].replace('\'' '\"', '', 2)
        # print(source_path)
        destination_path = sys.argv[2].replace('\'' '\"', '', 2)
        # print(destination_path)


# function to check if the given paths exist
def check_path():
    if not os.path.isdir(source_path):  # check that the path returns True
        print('The source path %s does not Exist' % source_path)
        sys.exit()
    if not os.path.isdir(destination_path):  # check that the path returns True
        print('The destination path %s does not Exist' % destination_path)
        sys.exit()


def drop_files(source, destination):
    files = os.listdir(source)
    global drop_count
    for file in files:
        shutil.copy2(f'{source}/{file}',destination)
        drop_count += 1
    print('%d files dropped' % drop_count)


def main():
    check_arg()
    check_path()
    drop_files(source_path, destination_path)
    print(now)


# run command
if __name__ == '__main__':
    main()
