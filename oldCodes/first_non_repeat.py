def first_non_repeat(s):
    if len(s) < 2:
        return s
    i = 0
    while i < len(s):
        j = len(s) -1
        while j >= i+1:
            if s[i] == s[j]:
                break
            if j == i+1:
                return s[i]
            j -= 1
        i += 1


print(first_non_repeat('asdfsdafdasfjdfsafnnunlfdffvxcvsfansd'))