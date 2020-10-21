'''
def spam():
    print(eggs) #biến eggs đc coi là biến toàn cục
eggs = 42
spam()
print(eggs)
'''

#=================================================================================================

'''
def spam():
    eggs = 'spam local' #biến eggs lại đc coi là biến địa phương vì ta đã khai báo eggs = ...
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) # prints 'global'
'''

#=================================================================================================

'''
def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'
eggs = 'global'
spam()
'''

#=================================================================================================
#Using global var in function

'''
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
'''

