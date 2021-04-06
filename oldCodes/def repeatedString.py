def repeatedString(s, n):
    print(s.count('a'))
    print((n // len(s)))
    print(s[:n% len(s) ].count('a'))
    return( ( s.count('a') * (n // len(s)) ) + s[:n% len(s) ].count('a') )




s = 'epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'
n = 549382313570
print(repeatedString(s, n))


#print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
16481469408