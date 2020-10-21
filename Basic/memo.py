#1,Chuyển char thành số và ngc lại
#print(ord('A'), chr(67)) 

#2, In ra các đường dẫn đến các package trên terminal
#echo $PATH;
#which python3;  

#3, In ra các x chữ số sau dấu thập phân
#print("{0:.3}".format(5 / 3));
#   Làm tròn kết quả đến x chữ số sau dấu thập phân
#print(round(132.1234172, 6))

#4, Swap 2 phần tử 
#x, y = 5, 10; x, y = y, x; print(x, y)

#5, Không biết phải input bao nhiêu dòng
'''
import sys
for line in sys.stdin:
    if line != '\n'
    print(line)
'''
#coi sys.stdin như một list chứa các dòng của file input ngoài ra nó tự động append thêm kí tự '\n' vào mỗi phần tử trong list
#nên khi ta gặp kí tự '\n' ta biết là hết file input và sẽ break raformat

#6, 

for i in range(10):
    print("{} and square is {}".format(i, i * i))