#check if 'character' is within the strings contained in 'lista'
#if an element in 'lista' is not a string then skips it
def findCharacter (lista, character):
    newList = []
    for element in lista:
        if type(element) != str:
            continue
        elif character in element:
            newList.append(element)
    print 'The folliwng strings in your list contain the character "' + character + '" ', newList

word_list = ['hello','world','my','name','is',0]
char = 'a'

findCharacter (word_list, char)