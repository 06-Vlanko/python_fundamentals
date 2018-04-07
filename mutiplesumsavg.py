#Part I, prints all odd nuybers from 1 to 1000, abusing the definition of odd numbers
#we increment count in +2 in each iteration and start counting from 1
def printOdds ():
    for count in range (1, 1000, 2):
        print(count)
#printOdds()

#Part II, print all multiples of 5 from 1 to 1 000 000
#starting from 5 we add 5 to count in each iteration
def printMultiplesOf5 ():
    for count in range (5, 100,5):
        print(count)
#printMultiplesOf5()

#Sum List, prints the summ of all values in a given list
def sumValues (arr):
    total = 0
    #elementy becomes the value stored in arr[n] where n is the current iteration number ( 1,2,3...(len(arr)-1) )
    for element in arr:
        total += element
    return total
#print (sumValues ([1, 2, 5, 10, 255, 3]))

#prints the average of the values in a list
def listAverage (arr):
    #adding 0.0 to allow exact average of odd/non integer numbers
    average = sumValues (arr) + 0.0
    average = average/len(arr)
    print average
listAverage ([1, 2, 5, 10, 255, 3])