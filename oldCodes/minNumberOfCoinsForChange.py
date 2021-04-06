def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    if n == 0:
        return -1
    denoms.sort()
    ways = [float('inf') for i in range(n +1)]
    ways[0] = 0
    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                ways[amount] = min(ways[amount], (ways[(amount - denom)] + 1))
    print(ways)
    return ways[len(ways) - 1] if ways[len(ways) - 1] != float('inf') else -1


print(minNumberOfCoinsForChange(7, [2, 4]))