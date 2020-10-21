'''
    Tìm nghiệm của phương trình A * x + B * y = gcd(A, B)
    Gọi x1, y1 là nghiệm của: A * x1 + B * y1 = a
        x2, y2 là nghiệm của: A * x2 + B * y2 = b
    Với a, b = q, r sau mỗi lần lặp tìm gcd
'''

def euclid_expand(a, b):
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while b != 0: 
        q = a // b 
        r = a % b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
        a, b = b, a - b * q 
        print(a, b, x1, x2, y1, y2)
    return [x1, y1, a]

print( euclid_expand(18648, 1261))