a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

count = 0

if a < 0:
    count += 1
if b < 0:
    count += 1
if c < 0:
    count += 1

print ("Количество отрицательных чисел среди a,b,c =", count)