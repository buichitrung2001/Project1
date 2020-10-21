#! /home/straw/miniconda3/bin/python3
# 2 kiểu sort
# list.sort(key = ..., reverse = ...)
# list2 = sorted(list, key = ..., reverse = ...)
# key: hàm so sánh
# reverse: nếu true sort ngược lại  

#=================================================================================================
# Dùng reverse:
arr = ['u', 'e', 'o', 'a', 'i']
arr2 = sorted(arr, reverse = True)
print(*arr2)
print(*arr)

#=================================================================================================
# Dùng key:

def sap_xep_theo_ki_tu_2(ten_anime):
    return ten_anime[2]

name = ['Naruto', 'FairyTail', 'Conan', 'AttackOnTitan', 'OnePiece']
name.sort(key = sap_xep_theo_ki_tu_2)
print(*name)