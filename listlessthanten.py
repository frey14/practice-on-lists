'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the
list that are less than 5.'''

mylist= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist=[]
for i in range(11):
    if(mylist[i]<10):
        newlist.append( mylist[i])
print(newlist)
        
