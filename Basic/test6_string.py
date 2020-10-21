## ! /usr/bin/python3
#================================================================================
#Escape characters: \
print('This is Trung\'s laptop')
print('This is Trung\" laptop')
print('This is Trung\t laptop')
print('This is Trung\n laptop')

#Raw string: r
print(r'This is Trung\\ laptop')

#================================================================================
#Upper, lower
str = 'BuiNguyenAnhMinhThuAnh'
str = str.upper()
print(str)
str = str.lower()
print(str)
print(str.isupper(), str.islower())

#split, join, strip
print('___'.join(['Sa', 'rang', 'heyo']))
print('TôizsẽztrởzthànhzVuazHảizTặc'.split('z'))
# loại bỏ tất cả kí tự hậu tô, tiền tố trong danh sách 
print('...abcd_Trungcd'.strip('.abcd_'))

#rjust, ljust, center   
print('ABC'.rjust(7, '_'))
print('ABC'.ljust(7, '_'))
print('ABC'.center(7, '_'))

#pyperclip
# import pyperclip
# pyperclip.copy('dumamay')
# print(pyperclip.paste())

