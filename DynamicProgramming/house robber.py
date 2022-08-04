# def house_robber(arr):
#
#     n = len(arr)
#
#     def rob(i):
#         if i < 0:
#             return 0
#         return max(rob(i - 2) + arr[i], rob(i - 1))
#
#     return rob(n - 1)
#
#
# a = list(map(int, input().split()))
# print(house_robber(a))
#
#
# def house_robber2(arr):
#     n = len(arr)
#
#     dp = [0] * (n + 2)
#
#     for i in range(n - 1, -1, -1):
#         dp[i] = max(dp[i] + dp[i - 2], dp[i - 1])
#
#     return dp[n - 1]
#
#
# a = list(map(int, input().split()))
# print(house_robber2(a))
#

# brute force top-down dfs
def house_robber(arr):
    pass
    n = len(arr)

    def dfs(i):
        if n <= i:
            return 0

        return arr[i] + max(dfs(i + 2), dfs(i + 3))

    return max(dfs(0), dfs(1))


# a = list(map(int, input().split()))
# print(house_robber(a))


# bottom-up dp
def house_rob(arr):
    n = len(arr)

    dp = [0] * (n + 3)

    for i in range(n -1, -1, -1):
        dp[i] = arr[i] + max(dp[i + 2], dp[i + 3])

    return max(dp[0], dp[1])


# a = list(map(int, input().split()))
# print(house_rob(a))


# bottom-up memory optimization
def house_robb(arr):
    n = len(arr)

    arr = arr + [0] * 3
    for i in range(n - 1, -1, -1):
        arr[i] += max(arr[i + 2], arr[i + 3])
    return max(arr[0], arr[1])


a = list(map(int, input().split()))
print(house_robb(a))
