##def fibonacci_recursive(n):
##    if n<=1:
##        return n
##    else:
##        return(fibonacci_recursive(n-1)+ fibonacci_recursive(n-2))
###example usage to print the first 10 terms:
##nterms=10
##if nterms<=0:
##    print("Please enter a positive integer")
##else:
##    print("Fibonacci sequence:")
##    for i in range(nterms):
##        print(fibonacci_recursive(i))
        

#fibonacci iterative
def fibonacci_iterative(n_terms):
    n1,n2=0,1
    count=0
    if n_terms<=0:
        print("Please enter a postive integer")
    elif n_terms==1:
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count <n_terms:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count +=1
fibonacci_iterative(7) #prints:0,1,1,2,3,5,8
