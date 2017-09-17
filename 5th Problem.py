def factorial(n):
    if n == 0:
        return 1;
    else:
        return n * factorial(n - 1)

def main():
    upperBound = factorial(20)
    lowerBound = 2520 * 11 * 13 * 17 * 19
    for i in range(lowerBound, upperBound, 20):
        counter = 0
        for j in range(1, 21):
            counter = j
            if i % j != 0:
                break
        if counter == 20:
            print(i)
            return 0
    return 1

main()