def dictionaryBasics (dictionary):
    for key, data in dictionary.iteritems():
        print 'My', key, 'is', data

aboutMe = {
    'Name' : 'Gerardo',
    'Age' : 33,
    'Birth Country' : 'Costa Rica',
    'Favorite Language' : 'Espaniol'
}

dictionaryBasics (aboutMe)