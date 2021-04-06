def sumDigits(n):
    if n <= 9:
        return n
    else:
        n = sum(map(int, list(str(n))))
        return sumDigits(n)


print(sumDigits(439230))