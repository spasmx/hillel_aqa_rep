# Task1
# Write a change(lst) function that takes a list and swaps its first and last element.
# The original list has at least 2 elements.


def change(lst):
    if len(lst) < 2:
        return 'list length must be greater than 1'
    change_elem_lst = lst[1:-1]
    change_elem_lst.insert(0, lst[-1])
    change_elem_lst.append(lst[0])
    return change_elem_lst


# Task2
# Write a function to_dict(lst) that takes a list argument and returns a dictionary in which each element of the
# list in both a key and a value. It is assumed that the elements of the list will comply with the rules for
# specifying keys in dictionaries.


def to_dict(lst):
    if not isinstance(lst, list):
        return 'Object must be list'
    if len(lst) < 1:
        return 'list must be not empty'

    return {elem: elem for elem in lst if not isinstance(elem, (list, set, dict))}


# Task3
# Write a function sum_range(start, end) that sums all integers from 'start' to 'end' inclusive.
# If the user specifies the first number is greater than the second, simply swap them.


def sum_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return 'Value must be integer'
    return sum([num for num in range(start, end + 1)]) if start < end else sum([num for num in range(end, start + 1)])


# Task4
# Write a read_last(lines, file) function that will open a specific file and print the last lines in a file


def read_last(lines, file):
    if not isinstance(lines, int):
        return 'Value must be integer'
    if lines < 0:
        return 'Value must be a positive integer'

    with open(file) as f:
        list_lines_file = f.readlines()[::-1]
        last_lines = []
        if lines > len(list_lines_file):
            return 'Error. Row count exceeded'

        for line in list_lines_file[:lines]:
            last_lines.append(line)

    return ''.join(reversed(last_lines))




