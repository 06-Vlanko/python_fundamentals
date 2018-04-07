#prints a checkbord pattern of 8 lines, if the number of the line is odd
#it will print a line with a space before the *
def checkerBoard ():
    for line in range (8):
        if line%2 == 1:
            print ' * * * *'
        else:
            print '* * * *'

checkerBoard()