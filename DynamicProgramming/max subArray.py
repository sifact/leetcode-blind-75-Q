# def max_product(nums):
#     n = len(nums)
#
#     mx = nums[0]
#     cur = 0
#     for i in range(n - 1):
#
#         cur += nums[i] * nums[i + 1]
#         if cur < 0:
#             cur = 0
#         mx = max(mx, cur)
#
#     return mx
#
#
# a = list(map(int, input().split()))
# print(max_product(a))


t = 2

for _ in range(2):
    x = int(input())
    add = 0
    while x:

        tmp = x % 10
        print(tmp, end='')
        x //= 10
    print()

