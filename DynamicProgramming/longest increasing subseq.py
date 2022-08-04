# Dfs tree
#                     [1,               2,          4,      3]
#                      |                |           |       |
#                     [1]              [2]          [4]      [3]
#                 /    |    \
#   `      [1, 2]  [1, 4]   [1, 3]
#         /     \
#  [1, 2, 4]  [1, 2, 3]
#

# dfs implementation

def longest_iss(nums):

    def dfs(arr, prev):
        if not arr:
            return 0
        longest = 0

        for i in range(len(arr)):
            if arr[i] > prev:
                curr = 1 + dfs(arr[i + 1:], arr[i])
                longest = max(longest, curr)
        return longest

    return dfs(nums, -float("inf"))


# a = list(map(int, input().split()))
# print(longest_iss(a))

# dp


def length_of_lis(nums):
    dp = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


a = list(map(int, input().split()))
print(length_of_lis(a))


