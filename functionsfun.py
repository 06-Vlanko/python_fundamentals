#counts from 1 to 2000 and prints if the current number is even or odd
def oddEven ():
    for counter in range (2001):
        if counter%2 == 0:
            print 'Number is', counter, ',an is an even number'
        else:
            print 'Number is', counter, 'an is an odd number'
#oddEven()

#takes a list arr (non decimal numbers only) and multiplies each of its values by multiplier
def multiply (arr, multiplier):
    newList = []
    for item in arr:
        newList.append (item*multiplier)
    return newList

#print multiply([2,4,10,16],5)

def multiply (arr):
    for x in range (len(arr)):
        arr[x] *=5
    print arr

multiply([2,4,10,16])

#takes an array of non decimal numbers and creates a new array containing of 1s * arr[i] for each element in arr
def layeredMultiples (arr):
    newList = []
    tempList = []
    for item in arr:
        for number in range (item):
            tempList.append(1)
        newList.append(tempList)
        tempList = []
    return newList

#print layeredMultiples( multiply([2,4,5],3) )