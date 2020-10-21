def dp012_flipping_game(n, a) :
    a.insert(0, 0)
    one, res, mn, dp = 0, 0, 0, [0]

    for i in range(1, n + 1) :
        dp.append(dp[i - 1])
        if (a[i] == 1) : 
            one += 1
            dp[i] -= 1
        else : dp[i] += 1

    for i in range(1, n + 1) :
        res = max(res, one + dp[i] - mn)
        mn  = min(mn, dp[i])
    return res


if __name__ == '__main__' : 
    n = int(input())
    a = list(map(int, input().split()))
    print(dp012_flipping_game(n, a))