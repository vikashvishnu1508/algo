def reverse_only_alpha(s):
      # fill in
    new_s = [i for i in s if i.isalpha()]
    new_s = reverse_array(new_s)
    s = list(s)
    j = 0
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = new_s[j]
            j += 1
    return ''.join(s)

def reverse_only_alpha2(s):
    new_s = list(s)
    start = 0
    end = len(new_s) - 1
    while start < end:
        if not new_s[start].isalpha():
            start += 1
        elif not new_s[end].isalpha():
            end -= 1
        else:
            new_s[start], new_s[end] = new_s[end], new_s[start]
            start += 1
            end -= 1
    return ''.join(new_s)

def reverse_array(arr):
      return arr[::-1]

print(reverse_only_alpha("sea!$hells3"))
# 'sll!$ehaes3'