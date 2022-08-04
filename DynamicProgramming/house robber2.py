def house_robber2(arr):

    if len(arr) == 1:
        return arr[0]

    def helper(nums):
        n = len(nums)

        nums += [0] * 3

        for i in range(n - 1, -1, -1):
            nums[i] += max(nums[i + 2], nums[i + 3])

        return max(nums[0], nums[1])

    return max(helper(arr[1:]), helper(arr[:-1]))


a = list(map(int, input().split()))
print(house_robber2(a))

