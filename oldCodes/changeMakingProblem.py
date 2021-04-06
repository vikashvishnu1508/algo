def changeMakingProblem(coins, amount):
    coinCount = {}
    coins.sort(reverse=True)
    i = 0
    while amount > 0:
        if amount - coins[i] < 0:
            i += 1
        else:
            amount -= coins[i]
            if coins[i] in coinCount:
                coinCount[coins[i]] += 1
            else:
                coinCount[coins[i]] = 1
    return coinCount


print(changeMakingProblem([1,3,5,7], 54))