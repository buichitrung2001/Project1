'''
import first_module
print(f"Second_module's name: {__name__}")
print(first_module.main())
print(first_module.plus(5, 10))
'''

#module first_module sẽ được tìm trong list các thư mục ở biến sys.path
import sys
#import module ở vị trí tùy ý, ngoài ra có thể thay đổi biến $PATH (google)
sys.path.append("/home/straw/Python/custom_module")
print(sys.path)

#có thể import cả biến toàn cục
from sub_module import minus, global_var

print(global_var, minus(10, 98))

