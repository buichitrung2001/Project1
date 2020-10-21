#https://www.w3schools.com/python/python_sets.asp

player = {'messi', 'ronaldo', 'pogba', 'bruyne'}
for i in player:
    print(i)
#các phần tử trong set sẽ được in ra theo thứ tự bất kì 

#================================================================================
print('xavi' not in player)
#thêm 1 phần tử
player.add('de jong')

#thêm nhiều phần tử 
player.update(['modric', 'busquest', 'neymar', 'mbappe'])
print(player, len(player))

#xóa phần tử
if 'ramos' in player:
    player.remove('ramos')   #bị lỗi nếu ko có phần tử bị xóa trong set
else:
    player.discard('ramos')  #giống hệt remove nhưng ko bị lỗi 
player.pop()                 #xóa phần tử cuối trong set nhưng kbiet là phần tử nào

#xóa cả set: clear

#hợp 2 set: update - set mới không chứa các phần tử giống nhau
player2 = {'ronaldo', 'xavi', 'iniesta'}
player.update(player2)
print(player)

