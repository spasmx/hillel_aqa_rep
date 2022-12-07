import random
# Task1
# Given a file with arbitrary text, you need to find all the numbers in the file and write them to the numbers list

with open('C:/Users/user/example.txt') as f:
    file = ' '.join(f.readlines())
    numbers = [num for num in file.split(' ') if num.isdigit()]
print(numbers)

# Task2
# Ask the user for text and write it to the data.txt file

with open('data.txt', 'w') as f:
    text = input('Enter some text: ')

    f.write(text)

# Task3
# Ask the user for the number N and ask for N numbers from the user, then write them to the numbers.txt
# file separated by a space

with open('numbers.txt', 'w') as f:
    count_of_num = int(input('Enter a count of number: '))
    numbers_list = ' '.join([str(int(input('Enter num: '))) for i in range(count_of_num)])

    f.write(numbers_list)

# Task4
# Generate 100 random numbers and write them to the random_numbers.txt file, where one line = one number

with open('random_numbers.txt', 'w') as f:
    random_numbers = []

    for i in range(100):
        num = str(random.randint(1, 9999)) + '\n'
        random_numbers.append(num)

    f.write(''.join(random_numbers))

# Task5
# Given a file with arbitrary text, you need to find the number of words in the file and display to the user

with open('C:/Users/user/example.txt') as f:
    file = ' '.join(f.readlines())
    words = [num for num in file.split(' ') if not num.isdigit()]
    print(len(words))
#
# Task6
# Given a file in which numbers are written separated by a space,
# it is necessary to display the sum of these numbers to the user

with open('C:/Users/user/example.txt') as f:
    numbers = f.read().split(' ')
    sum_of_num = sum([int(i) for i in numbers if i.isdigit()])
    print(sum_of_num)

# Task7
# Given a file in which the text is written, you need to display the top 5 lines that are most often repeated,
# for example:
# 'in' - 20 times
# 'hello' - 10 times
# 'how' - 9 times
# 'y' - 7
# 'world' - 4

with open('C:/Users/user/example.txt') as f:
    count_word = {}
    file = ' '.join(f.readlines()).replace('\n', '').split(' ')

    for word in file:
        count_word[word] = file.count(word)

    sorted_count_word = sorted(count_word.items(), key=lambda kv: kv[1], reverse=True)[:5]

    for word, count in sorted_count_word:
        print(f'{word} repeat {count} times')








