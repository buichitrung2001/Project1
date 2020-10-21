import scrapy 

#1, Khi dùng biến toàn cục
'''
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
'''

#2, Khi dùng biến toàn cục, có thay đổi giá trị biến

def spam():
    global eggs
    eggs = 100
    print(eggs)
eggs = 42
spam()
print(eggs)
