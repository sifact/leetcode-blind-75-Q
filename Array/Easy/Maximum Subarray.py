def max_sub_array(nums):
    max_cur = max_glob = nums[0]

    for i in range(1, len(nums)):
        max_cur = max(max_cur + nums[i], nums[i])

        max_glob = max(max_glob, max_cur)

    return max_glob


def max_sub_array2(nums):

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(dp[0] + nums[1], nums[1])  # 3 -1

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


num = list(map(int, input().split()))
print(max_sub_array2(num))
