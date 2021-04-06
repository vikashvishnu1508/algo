import math
def sockMerchant(ar):
    result = 0
    for i in set(ar):
        pair = math.floor(ar.count(i) / 2)
        if math.floor(ar.count(i) / 2) > 0:
            result += int(pair)
    return result

arr = [1,2,1,2,3,2,1,1]
print(sockMerchant(arr))