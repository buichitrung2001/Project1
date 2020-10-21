class laptop :
    def __init__(x, _price, _quality) :
        x.price = _price
        x.quality = _quality
    def __lt__(x, y) : 
        if x.price == y.price : return x.quality > y.quality
        return x.price > y.price

def solve(n, arr) :
    arr.sort()
    min_quality = 2 ** 31 + 1
    for i in arr : 
        if i.quality > min_quality : return True
        min_quality = min(min_quality, i.quality)
    return False

def laptops(n, arr) :
    if solve(n, arr) == True : print("Happy Alex")
    else : print("Poor Alex")

if __name__ == '__main__' :
    n = int(input())
    arr = []
    for i in range (n) :
        a, b = list(map(int, input().split()))
        arr.append(laptop(a, b))
    laptops(n, arr)