#Find and Replace
def findReplace ():
    words = "It's thanksgiving day. It's my birthday, too!"
    position = words.find('day')

    print(position)
    words = words.replace('day', 'month')
    print words

#findReplace()

#Min and Max
def minMax (arr):
    for element in arr:
        if type(element)!= int and type(element)!=float:
            print('Use only numbers in your array!')
            break
    else:
        minimum = min(arr)
        maximum = max(arr)
        print(minimum, maximum)

#minMax([1,2,3,-4,2.54])

#First and Last
def firstLast (array):
    print array[0]
    newArray = []
    if not array:
        return 'Your array is empty! >.<"'
    else:
        newArray.append(array[0])
        newArray.append(array[len(array)-1])
    return newArray

#print(firstLast(['hello',2,54,'world',98]))

#New List
def newList (arr):
    arr.sort()
    newArr1 = []
    newArr2 = []
    for index in range (0,len(arr)):
        if index < len(arr)/2:
            newArr1.append(arr[index])
        else:
            newArr2.append(arr[index])
    newArr2.insert(0,newArr1)
    print arr
    print newArr1
    print newArr2

array = [19,2,54,-2,7,12,98,32,10,-3,6,100]
newList (array)