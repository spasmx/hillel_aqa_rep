# task 1
# The user enters a word, if this word is a polyndrom, then output '+', otherwise '-'
palindrom = input('Enter your word: ')

if palindrom == palindrom[::-1]:
    print('+')
else:
    print('-')

# task 2
# The user enters the text and the word to be found, if this word is in the text, output 'YES', otherwise 'NO'
text = input('Enter your text: ')
word = input('Enter your word: ')

if text.find(word) != -1:
    print('YES')
else:
    print('NO')

# task 3
# The user enters a string. If it starts with 'abc', then replace them with 'www',
# otherwise add 'zzz' to the end of the string
user_string = input('Enter your text: ')

if user_string.startswith('abc'):
    user_string = user_string.replace('abc', 'www')
    print(user_string)
else:
    user_string += 'zzz'
    print(user_string)

# task 4
# The user enters text, remove all numbers in the text, and output a string to the user.
num_text = input('Enter your text: ')

for num in num_text:
    if num.isdigit():
        num_text = num_text.replace(num, '')
print(num_text)

# task 5
# Write a validator for mail. The user enters the mail, and the program must check that the mail contains
# the character '@' and '.', and if so, then print "YES", otherwise "NO"
email = input('Enter your email: ')

if email.count('@') == 1:
    if '.' in email:
        print('YES')
else:
    print('NO')
