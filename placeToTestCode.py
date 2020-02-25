""" Python 2.7 """

myList = [4,3,5,6,3,3]
# print(myList)

# "key" just needs to be there, don't overthink about it
myList.sort(key=lambda in1: in1%2)

# find the largest item in the 'list
# print( max(myList, key=myList.count) )
# print( max(set(myList), key=myList.count) )

for i in range(5):  # gives you a 'list' of number of 0 to 4
    print(i)