

def minRewards1(array):
    rewards = [1]
    runRange = 0
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            rewards.append(rewards[i - 1] + 1)
            runRange = i
        else:
            rewards.append(1)
            j = i - 1
            while j >= runRange:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)

def minRewards(array):
    rewards = [1 for i in range(len(array))]
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            rewards[i] = rewards[i - 1] + 1
    
    for i in range(len(array) - 2, 0, -1):
        if array[i] > array[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return sum(rewards)


array = [5, 10]

print(minRewards(array))