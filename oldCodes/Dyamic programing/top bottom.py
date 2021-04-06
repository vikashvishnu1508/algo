def fib(n, lookup):
    print("n = ", n)
    if n == 0 or n == 1 :
        lookup[n] = n
    if lookup[n] is None:
        print("i called fib (n) = ", n)
        lookup[n] = fib(n-1 , lookup) + fib(n-2 , lookup)
    #print("n = ",n)
    #print("lookup = ",lookup)
    return lookup[n]

def main():
    n = 34
    lookup = [None]*(35)
    print ("Fibonacci Number is ", fib(n, lookup))
    print(lookup)

if __name__=="__main__":
	main()