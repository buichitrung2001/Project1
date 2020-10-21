#================================================#
# OS module allow us to interact with the        #
# underlying operating system in several         #
# different ways                                 #
#================================================# 

import os
#print(dir(os))  

#===1, Trả về chô đang đứng===#
#print(os.getcwd())

#===2, Đổi chỗ đứng===#
#os.chdir('/home/straw/Đại_cương/Toan_roi_rac')

#===3, In danh sách file, folder===#
#print(os.listdir('/home/straw/Self_learn'))

#===4, Tạo, xóa dir===#
#os.mkdir('a') #tạo được 1 dir
#os.makedirs('a/b'/c/d) #tạo đc cả đường dẫn dir
#os.rmdir('a')
#os.removedirs('a/b/c/d')

#===5, Đổi tên===#
#os.rename('a.txt', 'b.txt')

#===6, In tất cả các dir, file con, có thể dùng để tìm file, dir ko nhớ vị trí===#
# for dirpath, dirs, files in os.walk('/home/straw/Đại_cương/Giai_tich_2'):
#     print('Current path: ', dirpath)
#     print('Directories: ', dirs)
#     print('Files: ', files)
#     print()

#===7, In biến môi trường===#
#print(os.environ.get('HOME'))

#===8, Join các thành phần lại thành path===#
#Để không bị quên các dấu '/'
#Trên win sẽ in ra các đường dẫn ngăn cách bởi dấu '\' nên lệnh chạy đc trên nhiều os.

# print(dir(os.path)) in các lệnh có trong os.path
# path = os.path.join(os.environ.get('HOME'), 'Cplus')
# print(path)

#===9, Kiểm tra path tồn tại k, là file hay dir===#
# print(os.path.exists('/home/straw/Đại_cương/Giai_tich_3'))
# print(os.path.isdir('/home/straw/miniconda3/bin'))
# print(os.path.isfile('/home/straw/miniconda3/bin'))

#===10, Tách phần mở rộng ===#
# print(os.path.splitext('/home/straw/Python/Learn_Python/Basic/test13_os_module.py'))

#===11, In biết môi trường===#
#print(os.getenv('DATABASE_URL'))