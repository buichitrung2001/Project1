# https://www.w3schools.com/
# https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python

# class cơ bản nhất
'''
class my_class :
    x, y = 0, 0.0

p = my_class()
print(p.x, p.y)
'''


# =================================================================================================

class jav_idol:
    skill = 10  # biến đc khai báo ở ngoài sẽ dùng chung cho mọi obj trong class(static)

    def __init__(self, _face, _body):  # class nào cũng phải viết hàm này để khởi tạo
        self.face = _face  # biến _face, _body là kiểu gì cself đc
        self.body = _body

    def get_face(self):
        return self.face

    def total(self):
        return self.face + self.body * 1.5

    def __lt__(self, y):
        return self.face < y.face


if __name__ == "__main__":
    julia = jav_idol(6, 8.5)
    emiri = jav_idol(9.5, 6)
    ichiki = jav_idol(8, 7.5)
    mikami = jav_idol
    print(julia.total())
    print(julia.skill)

    jav = [julia, emiri, ichiki]
    jav.sort();
    for i in (jav):
        print(i.face, i.body)
