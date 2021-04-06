def jumpingOnClouds(c):
    count = 0
    for i in range(len(c)):
        if c[i] == 0:
            if c[i + 1] == 0 and c[i + 2] == 0:
                count += count
                i += 2
            if c[i + 1] == 0:
                count += count
                i += 1
    return count

print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))