
# Memoization

def fib(n):
    d = {0: 0, 1: 1}

    if n < 2:
        return d[n]
    return fib(n - 1) + fib(n - 2)


# n = int(input())
# print(fib(n))


# dynamic programming

def fib2(n):
    dp = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


num = int(input())
print(fib2(num))
