#prints out an amout of * based on the current value of 'element'
def drawStars (arr):
    for element in arr:
        startString = ''
        for count in range (element):
            startString += '*'
        print startString

#drawStars ([2,3,4,1])

#prints out an amout of * based on the current value of 'element'
#if 'element' holds a string, it will print the first letter of the string len() amount of times
def drawStarsPlus (arr):
    for element in arr:
        startString = ''
        if isinstance (element, int):
            for count in range (element):
                startString += '*'
            print startString
        elif isinstance (element, str):
            for count in range ( len(element) ):
                startString += element[0]
            print startString

drawStarsPlus ([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
