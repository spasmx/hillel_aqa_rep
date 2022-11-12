number = int(input('Enter your number: '))
reversed_number = 0
if number > 999:
    print('too big number')
else:
    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
print(reversed_number)