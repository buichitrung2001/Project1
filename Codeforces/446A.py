dp_right, dp_left = [], []
def solve(n, a) : 
    a.insert(0, 0); a.append(0)
    for i in range (1000005) :
        dp_right.append(0)
        dp_left.append(0)

    res = 0
    for i in range(1, n + 1) :
        if a[i] > a[i - 1] : dp_right[i] = dp_right[i - 1] + 1
        else : dp_right[i] = 1 
        res = max(res, dp_right[i])

    for i in range(n, 1 - 1, -1) :
        if a[i] < a[i + 1] : dp_left[i] = dp_left[i + 1] + 1
        else : dp_left[i] = 1
        
    for i in range (1, n + 1) : 
        res = max(res, max(dp_right[i - 1] + 1, dp_left[i + 1] + 1))
        if a[i - 1] + 1 < a[i + 1] : res = max(res, dp_right[i - 1] + 1 + dp_left[i + 1])
    return res

def dp010_dzy_loves_sequences(n, a) : 
    return solve(n, a)

if __name__ == '__main__' : 
    n = int(input())
    a = list(map(int, input().split()))
    print(dp010_dzy_loves_sequences(n, a))