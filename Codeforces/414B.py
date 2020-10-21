#chạy test to nhất sẽ mất gần 10s
mod = 1000000007
def solve(n, k) : 
    dp = []
    for i in range(0, k + 1, 1) : 
        dp.append([])
        for j in range(0, n + 1, 1) : dp[i].append(0)
    for i in range(1, n + 1, 1) : dp[1][i] = 1

    for i in range(1, k - 1 + 1, 1) : 
        for j in range(1, n + 1, 1) : 
            if dp[i][j] == 0 : continue
            for l in range(j, n + 1, j) : 
                dp[i + 1][l] = (dp[i + 1][l] + dp[i][j]) % mod

    res = 0
    for i in range(1, n + 1, 1) : 
        res = (res + dp[k][i]) % mod
    return res


def dp008_mashmokh_and_acm(n, k) : 
    return solve(n, k)

if __name__ == '__main__' :
    n, k = list(map(int, input().split()))
    print(dp008_mashmokh_and_acm(n, k))