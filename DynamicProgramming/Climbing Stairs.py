# def climbing_stairs(num):
    #  base case
    # if num <= 2:
    #     return num
    # return climbing_stairs(num - 1) + climbing_stairs(num - 2)

    # dic = {1: 1, 2: 2}
    # if num not in dic:
    #     dic[num] = climbing_stairs(num - 1) + climbing_stairs(num - 2)
    #
    # return dic[num]

#     a, b = 1, 2
#
#     for _ in range(1, num):
#         a, b = b, a + b
#
#         return a
#
#
# n = int(input())
# print(climbing_stairs(n))


#  all possibilities are considered via brute-force top-down depth-first-search
def min_cost_climbing_stairs(a):
    pass
    n = len(a)

    def dfs(i):
        if n <= i:
            return 0
        return a[i] + min(dfs(i + 1), dfs(i + 2))

    return min(dfs(0), dfs(1))


# arr = list(map(int, input().split()))
# print(min_cost_climbing_stairs(arr))


# bottom-up dp
def min_cost_climbing_stairs2(a):
    n = len(a)

    dp = [0] * (n + 2)

    for i in range(n - 1, -1, -1):
        dp[i] = a[i] + min(dp[i + 1], dp[i + 2])

    return max(dp[0], dp[1])


arr = list(map(int, input().split()))
print(min_cost_climbing_stairs2(arr))


# bottom-up memory optimization:
def min_cost_climbing_stairs3(arr):
    n = len(arr)
    a, b, c = 0, 0, 0

    for i in range(n - 1, -1, -1):
        c = arr[i] + min(b, a)
        a = b
        b = c
    return min(b, a)


# arr = list(map(int, input().split()))
# print(min_cost_climbing_stairs3(arr))
