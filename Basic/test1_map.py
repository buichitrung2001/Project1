def binh_phuong(n) :
    return n * n
a = [5, 10, 15, 20]
b = (1, 2, 3, 4)

#Dùng def
'''
d, e, f, g = list(map(int, a))
res = list(map(binh_phuong, a))
print(*res, g)
'''

#=================================================================================================

#Hàm lambda
'''
res1 = list(map(lambda x: 6 * x, a))
res2 = tuple(map(lambda x, y: x * y, a, b))
print(res1, *res2, sep = '\n')
'''
