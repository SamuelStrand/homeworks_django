# Task 1
bilet = str(input())
sum1 = int(bilet[0]) + int(bilet[1]) + int(bilet[2])
sum2 = int(bilet[3]) + int(bilet[4]) + int(bilet[5])
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')

# Task 2

a, b = int(input()), int(input())
s = a
while s % a or s % b:
    s += a
print(s)
