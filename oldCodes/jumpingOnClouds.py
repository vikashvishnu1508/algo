def jumpingOnClouds(c):
    count = 0
    i = 0
    while(i < len(c)-1):
        #print(i+2)
        
        if i+2 <= len(c)-1 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count += 1
    return count


s = [0,0,1,0,0,1,0]
print(jumpingOnClouds(s))