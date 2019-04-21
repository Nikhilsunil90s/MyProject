#String ---- ''/""/''' '''/"""Multiline Strings""" --- sequences, ordered, indexed, immutable
#create ---
st = ""
st = 'This is a sample string!'
#Access ---- via indexes
print(st[9])
#Update ---- Immutable
#st[3] = 'o'
#Delete
del st
st = 'this is st'
print(st)
#del st[2]
#Operations ----
#Arithmetic --- +,*
print(st*3)
#Logical Operations, Comparisons, Membership Operations(in, not in), Identity Operations(is, is not)
#Iterations ----
#over the values
for x in 'rediff':
    print(x,end=' ')
print('\n')
#over the indexes
for x in range(len(st)):
    print(st[x],end=' ')
print('\n')
#Slicing ----- [beg:end-1:step]
string = 'SlicedString'
print(string[2:7])
#beg = default, 0
#end = default, len(str)-1
#step = default, 1
print(string[3:])
#Reverse a string
#two way indexes ---
string = 'sample string'
print(string[-2])
#Reverse using a for loop:
for x in range(-1,-len(string)-1,-1):
    print(string[x],end=' ')
#Reverse using slicing operators
print(string[::-1])
#Formatted strings
#x = 'hello',y='hey' ---- not allowed
x,y,z = 'hello',123.7655,'hey'
print('These are python data variable : {2},{0},{1}'.format(x,y,z))
print(f'These are python data objects: {x},{z},{y}')

    
































    


