# ordered sequences that can hold a variety of object types
# they use brackets and commas to separate objects in a list
# lists support indexing and slicing
# can be nested and also have a variety of useful methods that can be 
# called off of them
# lists are mutable

myList = [1,2,3]
myList = ["String", 100, 23.2]
len(myList)
myList = ["one", "two", "three"]
myList[0]
myList[1:]
anotherList = ["four", "five"]
myList + anotherList
newlist = myList + anotherList

newlist[0] = "ONE"
newlist.append("six")
newlist.append("seven")
newlist.pop()
poppedItem = newlist.pop()
newlist.pop(0)

newlist = ["a", "e", "x", "b", "c"]
numList = [4,1,8,3]
newlist.sort()
numList.sort()
numList.reverse()
