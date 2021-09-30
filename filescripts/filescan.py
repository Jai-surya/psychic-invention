import sys
import os
from datetime import *

# Global Variables
path = ''
db_file = ''
now = datetime.now()
filecount = 0


# db_file = "file_names.txt"

# check the input command
def check_arg():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Script command format is :')
        print('<python> <filename.py> <directory_path> <out_file>')
        exit()
    else:
        global path
        path = sys.argv[1].replace('\'' '\"', '', 2)  # removes the '' and "" from the pass in arg


def out_file():
    if len(sys.argv) == 3:
        global db_file
        db_file = sys.argv[2]
    else:
        db_file = "file_names.txt"


# read file names in path directory and store in file
def files(self):
    arr = os.listdir(self)
    for item in arr:
        f = open(db_file, 'a+', encoding="ascii", errors="backslashreplace")
        f.seek(0)
        lines = f.read().splitlines()
        if item in lines:
            print(item + ' exists in DB file ' + db_file)
        else:
            f.write(item + '\n')
            global filecount
            filecount += 1
        f.close()
    print('NUmber of new files : ', filecount)

# main function
def main():
    check_arg()
    out_file()
    files(path)
    print('Timestamp : ', now.strftime("%m/%d/%Y, %H:%M:%S"))

# Executing Command
if __name__ == '__main__':
    main()
