def word_break(word_dict, s):
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True

    for i in range(n - 1, -1, -1):
        for w in word_dict:
            if i + len(w) <= n and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]


wd_dict = list(input().split())  # ['leet', 'code']
string = input()  # leetcode
print(word_break(wd_dict, string))

