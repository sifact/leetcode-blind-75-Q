def find_target(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False


def find_min(nums):
    pass


num = list(map(int, input().split()))
n = int(input())
print(find_min(num, n))
