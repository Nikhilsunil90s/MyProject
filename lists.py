#lists ---- arrays, sequential DS, heterogenous collection, ordered, indexed(0), mutable
#int array[90];
#create
li = [1,2,3,4,8.9,"String","c"]
print(li)
#access ---
print(li[5])
#update ----
li[6] = 'updated value'
print(li)
#delete
del li[1]
print(li)
#operations ----
#Arithmetic Operations ---- +,*(int)
print(['a','b','c']+[1,2,3,4])
print(['hey','hello']*6)
#Comparisons ---- <,>,<=,>=,==,!=
print([1,2,3,4,5]<[1,2,3,4,5,6,7,8,9] and ['a'] != ['b','c'])
print(len([1,2,3,4,5,6,7,8,8,9]))
#Logical Operations --- and, or, not
#Membership Operations ---- in, not in
print('apple' in ['apple','banana','red'])
#identity Operations -- is, is not
Empty_list = []
#----------------------------------------------------
#Iterations ---- 1. Over the values, 2. Over the indices
for x in [1,2,3,4,4,6]:
    print(x)

#
li = [1,2,3,4,5,6,7,8,9]
for x in range(0,len(li)):
    print(li[x], end = ' ')
#Like Strings, Lists can also be reverse iterated
#Lists indices works both way
#Slicing ---- [:end-1:]
print(li[3:6])
print(li[::-1])
#Nested Lists -------
nested_list = [1,2,3,4,['a','b',"c"],5,6,7,8,[19,18,17,16,['d','e','f']]]

print(nested_list[4][2])
print(nested_list[9][4][2])

#List Comprehensions ---- Dynamic Lists
li = [r for r in range(20)]
print(li)

li = [i for i in 'python']
print(li)
#To take multiline inputs in python -------
li = [input() for i in range(3)]
print(li)

#x = input("Enter Some: ")
#print(x)

