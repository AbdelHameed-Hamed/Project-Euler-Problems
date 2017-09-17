def isPalindrome(text):
    if len(text) < 1:
        return False
    for i in range(0, int(len(text)/2)):
        if (text[i] != text[(len(text) - 1) - i]):
            return False
    return True

def main():
    factor1 = 999
    factor2 = 999
    maxPalindrome = 0
    for i in range(factor1, 100, -1):
        for j in range(factor2, 100, -1):
            product = i * j
            if isPalindrome(str(product)) and product > maxPalindrome:
                print(str(product) + " " + str(i) + " " + str(j))
                maxPalindrome = product
    return 1

main()