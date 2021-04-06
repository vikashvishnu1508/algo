def uglyNum(n):
    count = 3
    i = 4
    while count<n:
        if i%2 == 0 or i%3 == 0 or i%5 == 0:
            count += 1
        i += 1
    return i -1

print(uglyNum(10))