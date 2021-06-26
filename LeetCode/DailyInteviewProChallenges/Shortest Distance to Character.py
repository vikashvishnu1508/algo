def shortest_dist(s, c):
    shortest_distArray = [0 for i in s]
    positionsOfC = []
    for i in range(len(s)):
        if s[i] == c:
            positionsOfC.append(i)
    
    leftCharPos = -float('inf')
    rightCharPosIdx = 0
    rightCharPos = positionsOfC[rightCharPosIdx]
    for i in range(len(s)):
        if s[i] == c:
            if rightCharPosIdx == len(positionsOfC) - 1:
                rightCharPosIdx = float('inf')
                continue
            leftCharPos = positionsOfC[rightCharPosIdx]
            rightCharPos = positionsOfC[rightCharPosIdx + 1]
            rightCharPosIdx += 1
            continue

        curLeftDiff = i - leftCharPos
        curRightDiff = rightCharPos - i
        shortest_distArray[i] = min(curLeftDiff, curRightDiff)

    return shortest_distArray

print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]