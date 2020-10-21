from math import gcd


def euclid_expand(a, b):
    A = a
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while b != 0: 
        q = a // b 
        r = a % b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
        a, b = b, a - b * q 
    return (y1 + A) % A