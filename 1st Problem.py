summ = 0
for num in range(3, 1000):
    if (num % 3 == 0 or num % 5 == 0):
        summ += num
print(summ)