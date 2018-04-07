#prints all the values contained within the dictionaries of a list
def printNames (dictionary):
    #moves through the list, index becomes each of the dictionaries, one at a time
    for index in dictionary:
        fullName = ''
        #pulls the data for each key within index
        for data in index.itervalues():
            #str(data) converts data (which is tuple type) to str
            fullName += ' ' + str(data)
            

        print fullName

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
#printNames (students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printNamesPlus (dictionary):
    for value in dictionary.iterkeys():
        print value
        for index in range( len(dictionary[value]) ):
            #why output = index+1, '-' produces (1, '-')? update now it won't even work and will say index+1 is a tuple?
            output = str(index+1) + ' - '
            charNumber = 0
            for deepValue in dictionary[value][index].itervalues():
                output += deepValue.upper()+ ' '
                charNumber += len(deepValue)
            print output + '- ', charNumber

# def printNamesPlus (dictionary):
#     for value in dictionary.itervalues():
#         counter = 1
#         for index in value:
#             #why it thinks I'm creating a tupple when output = '', counter
#             output = '' + str(counter)
#             output += ' - '
#             charNumber = 0
#             counter += 1
#             for deepValue in index.itervalues():
#                 output += str( deepValue.upper() )
#                 output += ' '
#                 charNumber += len(deepValue)
#             print output, '-', charNumber

printNamesPlus(users)