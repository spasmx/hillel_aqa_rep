a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

if a > 10 and b > 10 and c > 10:
    if a % 3 == 0 and b % 3 == 0:
        print('yes')
else:
    print('no')
