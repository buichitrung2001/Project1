friends = ['An', 'HAnh', 'Long', 'Viet'] 
array = [[1, 2, 3], [4, 5, 6]] #mảng 2 chiều

#================================================================================
print(friends[1 : 2], end = ' ')
print(len(friends))
for i in friends:
    print(i, end = ' ')
del friends[2]
print(friends)

#================================================================================
if 'An' in friends: print('hahah')
if 'HAnh' not in friends: print('non')

print(friends.index('Viet'))

#================================================================================
friends.append('Long')
friends.insert(1, 'Hiep')
print(friends)
friends.remove('Hiep')
friends.sort()
friends.sort(reverse = True)
print(friends)

#================================================================================
name = 'BuiAnhThu'
name = list(name)
print(name)

#================================================================================
import copy
#ban = copy.copy(friends)
ban = friends.copy()
print(ban)
