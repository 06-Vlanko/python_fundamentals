import random

#generates a semi-random number between 60 to 100 and provies a letter Grade A for it
def scoresToLetters ():
    score = 0
    print 'Scres and Grades'
    for counter in range (10):
        score = random.randint(60, 100)
        if score >= 90:
            print 'Score:', score, "; Your grade is A"
        elif score >= 80:
            print 'Score:', score, "; Your grade is B"
        elif score >= 70:
            print 'Score:', score, "; Your grade is C"
        elif score >= 60:
            print 'Score:', score, "; Your grade is D"
    print 'All calculations completed, Bye~!'
        
scoresToLetters()