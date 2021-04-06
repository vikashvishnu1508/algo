def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + 1 == j + 1:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1
    return count



arr = [1, 3, 5, 2, 4, 6, 7]
print(minimumSwaps(arr))