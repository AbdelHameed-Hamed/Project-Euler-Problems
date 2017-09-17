summ = 0
fib1 = 1
fib2 = 2
while fib2 < 4E6:
    if (fib2 % 2 == 0):
        summ += fib2
    temp = fib2
    fib2 += fib1
    fib1 = temp
print(summ)