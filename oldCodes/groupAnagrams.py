def groupAnagrams(words):
    # Write your code here.
    result = []
    tempRes = []
    tempRes.append(words[0])
    i = 1
    while len(words) != 0:
        if isAnagram(words[0], words[i]):
            tempRes.append(words[i])
            words = words[:i] + words[i + 1:]
            i -= 1
        i += 1
        if i == len(words):
            result.append(tempRes[:])
            words = words[1:]
            i = 1
            tempRes = []
            if len(words) != 0:
                tempRes.append(words[0])
    return result

def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    dict1 = {}
    dict2 = {}
    i = 0
    while i < len(str1):
        if str1[i] in dict1.keys():
            dict1[str1[i]] += 1
        else:
            dict1[str1[i]] = 1
        if str2[i] in dict2.keys():
            dict2[str2[i]] += 1
        else:
            dict2[str2[i]] = 1
        i += 1
    if dict1 == dict2:
        return True
    return False

def groupAnagramAlgoMethod(words):
    sortedWords_LetterOnly = [''.join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    # sortedWords = sorted(sortedWords_LetterOnly)
    indices.sort(key = lambda x: sortedWords_LetterOnly[x])



print(groupAnagramAlgoMethod(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
