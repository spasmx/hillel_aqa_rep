
# Access rights
# The virus damaged the system of file permissions. It is known that certain actions can be performed on each file:
# entry - W;
# reading - R;
# launch - X.
# The input to the program is:
# the number n is the number of files;
# n lines with filenames and allowed operations;
# the number m is the number of requests to files;
# m requests of the type "file operation".
# For each valid request, the program should return OK, for invalid - Access denied.
import datetime

ACTIONS = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
    }

while count_files := input('Enter count files: '):
    if not count_files.isdigit():
        print('Value must be integer')
    else:
        count_files = int(count_files)
        break

files_and_operations = {}
for i in range(count_files):
    file_and_actions = input('Enter file name and actions that can be performed[W/R/X]: ').split(' ')
    files_and_operations[file_and_actions[0]] = file_and_actions[1:]


while count_operations := input('Enter count operations above files: '):
    if not count_operations.isdigit():
        print('Value must be integer')
    else:
        count_operations = int(count_operations)
        break

for i in range(count_operations):
    operation, file = input('Enter operations and file name: ').split(' ')
    try:
        if ACTIONS[operation] in files_and_operations[file]:
            print(f'File: {file}, Action: {operation}, '
                  f'Date: {datetime.datetime.now().strftime("%Y-%m-%d %X")}, Status: OK')
        else:
            print(f'File: {file}, Action: {operation}, '
                  f'Date: {datetime.datetime.now().strftime("%Y-%m-%d %X")}, Status: Access denied')
    except KeyError:
        print('FILE OR ACTION NOT FOUND')


