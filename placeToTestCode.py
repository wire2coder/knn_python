""" Python 2.7 """

myList = [4,3,5,6,3,3]
print(myList)

# "key" just needs to be there, don't overthink about it
myList.sort(key=lambda in1: in1%2)
print(myList)
