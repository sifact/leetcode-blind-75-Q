def jump_game(nums):
    pass
    n = len(nums)
    goal = n - 1

    for i in range(n - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if not goal else False


arr = list(map(int, input().split()))
print(jump_game(arr))
