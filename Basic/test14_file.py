#=================================================#
# Binaryfile: khi mở trong NotePad hay TextEditor #
# nhìn như mot đống cức.                          #
# VD: pdf, image, executable,executable programs  #
#                                                 #
# Plaintext: các file dễ đọc như .txt, .inp       #   
#                                                 #   
#=================================================#

#===1, Mở file===#
#file = open('/home/straw/Python/Learn_Python/Basic/test14_file.txt')

#===2, Đóng file===#
# Các lý do nên đóng file sau khi sử dụng:
# +) Mở nhiều file sẽ làm chậm máy, tốn RAM
# +) Trong windows, nó ko cho phép mở file ở một chương trình khác khi nó chưa đc đóng trước đó. 

#===3, Đọc file===#
# Coi cả file là một xâu
# data = file.read()

# Coi mỗi dòng là một xâu, tuy nhiến sẽ thêm kí tự '\n' vào cuối mỗi dòng(trừ dòng cuối)
# data = file.readlines()
# print(data)
# for line in data:
#    print(len(line), int(line))

#===4, Ghi file, muốn ghi trước hết phải mở file ===#
# Ghi đè lên data cũ
# file_name = open('test14_file_1.txt', 'w')
# file_name.write('Give me freedom, give me fire\n')
# file_name.close()

# Append lên data cũ
# file_name = open('test14_file_1.txt', 'a')
# file_name.write('Give me reason, take me higher\n')
# file_name.close()

#===5, with open ===#
with open("file_location", "file_mode", encoding = "utf-8") as file :
    pass
# ưu điểm: handle exceptions tốt hơn, tự động đóng file 