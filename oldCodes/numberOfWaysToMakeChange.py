def numberOfWaysToMakeChange(n, denoms):
    ways = [0 if i > 0 else 1 for i in range(n +1)]
    for i in denoms:
        for j in range(n + 1):
            if i <= j:
                ways[j] = ways[j] + ways[j - i]
    return ways[len(ways) - 1]


print(numberOfWaysToMakeChange(25, [1, 5, 10, 25]))
