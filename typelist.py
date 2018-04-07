def typeList (arr):
    string =''
    stringCounter = 0
    number = 0
    numberCounter = 0
    unknownTypeCounter = 0
    for index in arr:
        if type(index) == int:
            number += index
            numberCounter += 1
        elif type(index) == str:
            string += ''+index
            stringCounter += 1
        else:
            unknownTypeCounter += 1

    print (string)
    print (number)

    if stringCounter!=0 and numberCounter!=0:
        print ('The list you entered is mixed')
    elif stringCounter != 0:
        print ('The list you entered contains only strings')
    elif numberCounter != 0:
        print ('The list you entered contains only numbers')
    if unknownTypeCounter != 0:
        print ('The list you entered contains', unknownTypeCounter, 'unkown types')

typeList([0,-9,333333333333, 'stringo'])