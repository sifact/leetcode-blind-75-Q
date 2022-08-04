def max_product(nums):
    a, b = 0, 0

    for i in range(len(nums)):
        a = max(a, b)
        b = min(a, b)

        # -3 -1 -1


n = list(map(int, input().split()))
print(max_product(n))

