""" Python 2.7 """

myList = [4,3,5,6,3,3,2 ,1,3]
# print(myList)

# "key" just needs to be there, don't overthink about it
# myList.sort(key=lambda in1: in1%2)

# find the largest item in the 'list
# print(set(myList))
print( max(myList) ) # the MAXIMUM value in the 'group'
print(  )


# enumerate function
l1 = ["eat", "sleep", "repeat"]

# create 'enumerate object'
e1 = enumerate(l1)

# print(type(e1))     # >> enumerate
# print( list(e1) )   # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]


# Usually however, it's used to show we don't care about it's value. For example:
# It's considered appropriate here because we arnt using the value, we want to do something unrelated 10 times.
for _ in range(5):
    print("what")