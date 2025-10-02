#simple recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#memoization (top-down)
memo = {}
def fib(n):
    if n <= 1:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

#tabulation (bottom-up)
def fib(n):
    table = [0] * (n+1)
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

#constant space
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c   
    return c
