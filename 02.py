def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

first = 1
secound = 2

sum = 0

while (first < 4000000):

    if isEven(first):
        sum = sum + first
    new = first + secound
    first = secound
    secound = new

print(sum)
