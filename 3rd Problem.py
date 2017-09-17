bigNumm = 600851475143
sqrtBigNumm = int(bigNumm**0.5)
arr = [True] * sqrtBigNumm

for i in range(2, sqrtBigNumm):
    if arr[i - 1] == True:
        for j in range(i**2, sqrtBigNumm, i):
            arr[j - 1] = False

for i in range(sqrtBigNumm, 2, -1):
    if arr[i - 1] == True and bigNumm % i == 0:
        print(i)
        break