import time

start = time.time()

def Fibonacci(n):
    if n < 0:
        print("Incorrect input") 
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
fib = str(Fibonacci(35))

print ("fib(35) = " + fib)

end = time.time()
tok = str(end - start)

print("fib(35) took " + tok +" seconds")