a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))
max = 0
if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
elif c > a and c > b:
    max = c
print(max)
