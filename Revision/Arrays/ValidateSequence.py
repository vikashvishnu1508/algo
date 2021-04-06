def isValidSubsequence(array, sequence):
    currentSequenceIdx = 0
    for i in range(len(array)):
        if array[i] == sequence[currentSequenceIdx]:
            currentSequenceIdx += 1
    return currentSequenceIdx == len(sequence)





array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array, sequence))