while (width := int(input('Enter the width to create the triangle: '))) and width < 2:
    print('Enter a number greater than one')

star = '*'

#first triangle
for i in range(width, 0, -1):
    print(star * i)

#second triangle
for i in range(width + 1):
    print(star * i)

#third triangle
count1 = 0
for i in range(width, 0, -1):
    triangle = star * i
    print(' ' * count1 + triangle)
    count1 += 1

#fourth triangle
count2 = width
for i in range(width + 1):
    triangle = star * i
    print(' ' * count2 + triangle)
    count2 -= 1



