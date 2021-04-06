def minimumBribes(q):
    valid = False
    result = 0
    for i in range(0, len(q)-2):
        if q[i] == q[i + 2] + 1 and q[i+1] == q[i + 2] - 1:
            valid = True
            result += 2
        if q[i] == q[i+1] + 1:
            result += 1
    if not valid:
        return 'Too chaotic'
    return result


arr = [2, 5, 1, 3, 4]
print(minimumBribes(arr))