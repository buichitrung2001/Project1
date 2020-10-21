#dictionary trong python tương tự như unordermap trong c++
birthdays = {'dad': '3/3', 'mom':'14/08', 'sis': '17/12', 'me': '5/2'}

#================================================================================
for i in birthdays.keys(): print(i, end = ' ')
for i in birthdays.values(): print(i, end = ' ')
for i in birthdays.items(): print(i)
print(list(birthdays.keys()))

if 'dad' in birthdays.keys(): print('chuan cmnr')
if '3/3' in birthdays.values(): print('chuan cmnr')

birthdays.setdefault('grandmom', '1935')
for u, v in birthdays.items(): print(u, v)
