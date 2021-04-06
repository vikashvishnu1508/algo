import copy
def getPermutationsMethodOne(array):
    # Write your code here.
    perms = []
    permutationHelpermethodOne(array,[],perms)
    return perms

def permutationHelpermethodOne(array, perm, perms):
    if len(array) == 0:
        perms.append(perm)
    else:
        for num in range(len(array)):
            newArr = array[:num] + array[num + 1:]
            newPerm = perm + [array[num]]
            permutationHelper(newArr, newPerm, perms)

def getPermutations(array):
    perms = []
    permutationHelper(0, array, perms)
    return perms

def permutationHelper(index, array, perms):
    if index + 1 == len(array):
        perms.append(copy.copy(array))
    else:
        for j in range(index, len(array)):
            swap(index, j, array)
            permutationHelper(index + 1, array, perms)
            swap(index, j, array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    return array

print(getPermutations([1,2,3]))
