# task 1
# Ask the user for 5 numbers and write them into a list
num_list = []

while len(num_list) < 5:
    num = int(input('Enter your number: '))
    num_list.append(num)
    print(f'Remains to enter numbers {5 - len(num_list)}')
print(num_list)

# task 2
# Given a list A = [1, 2, 3, 4, 5]
# Remove the last number from the list
a = [1, 2, 3, 4, 5]
a.pop()
print(a)

# task 3
# Ask the user for 10 numbers and write them into list A
# Ask the user for the number N
# Display to the user how many times the number N is repeated in the list A
a = []

while len(a) < 10:
    num = int(input('Enter your number: '))
    a.append(num)
    print(f'Remains to enter numbers {10 - len(a)}')

n = int(input('Enter your number(counter): '))

print(f'Count of number {n} in your list = {a.count(n)}')

# task 4
# Ask the user for the number N
# Ask the user for N numbers and write them to list A
# List in reverse order
n = int(input('Enter your num: '))
list_n = []

while len(list_n) < n:
    num = int(input('Enter your number: '))
    list_n.append(num)
    print(f'Remains to enter numbers {n - len(list_n)}')

list_n.reverse()
print(list_n)

# task 5
# Ask the user for 5 numbers and write them to list A
# Write all numbers from list A that are greater than 5 into list C
a = []

while len(a) < 5:
    num = int(input('Enter your number: '))
    a.append(num)
    print(f'Remains to enter numbers {5 - len(a)}')

c = [i for i in a if i > 5]
print(c)

# task 6
# Ask the user for the number N
# Ask the user for N integers and write them to list A
# Find the minimum and maximum number in it using a loop (it is forbidden to use the min and max functions).
# Output these numbers.
n = int(input('Enter your num: '))
a = []

while len(a) < n:
    num = int(input('Enter your number: '))
    a.append(num)
    print(f'Remains to enter numbers {n - len(a)}')
print(a)
min_num = 0
max_num = 0
for i in a:
    min_num = i
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i

print(f'Min number in list {a} = {min_num}')
print(f'Max number in list {a} = {max_num}')

# task 7
# The user enters text, you need to display the number of numbers in this text
# Example:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Number of numbers: 3
user_text = input('Enter your text: ').split(' ')
count_of_number = 0
for number in user_text:
    if number.isdigit():
        count_of_number += 1
print(count_of_number)




