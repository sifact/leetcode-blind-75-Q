
# def coin_change(coins, amount):

    # def helper(coins, amount, add, arr):
    #     mx = 0
    #     if coins:
    #
    #         mx = max(coins)
    #         coins.remove(mx)
    #
    #     while True:
    #
    #         if add + mx > amount:
    #             return helper(coins, amount, add, arr)
    #
    #         add += mx
    #         arr.append(mx)
    #         if add == amount:
    #             return len(arr)
    # return helper(arr, amount, 0, [])

#     def dp(updated_amount):
#         if updated_amount == 0:
#             return 0
#         if updated_amount < 0:
#             return float("inf")
#
#         return min(dp(updated_amount - coin) + 1 for coin in coins)
#
#     return dp(amount) if dp(amount) != float("inf") else -1
#
#
# num = int(input())
# n = list(map(int, input().split()))
# print(coin_change(n, num))


def coin_change2(coins, amount):
    pass

    dp = [amount + 1] * (amount + 1)

    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1


num, arr = int(input()), list(map(int, input().split()))
print(coin_change2(arr, num))






















