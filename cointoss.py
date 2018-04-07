import random
#throws a coin 5000 times, and prints how many times you got tails or heads
def coinToss ():
    head = 0
    tail = 0
    coin = 0 #1 = head, 2 = tail
    for counter in range (5000):
        coin = random.randint (1,2)
        if coin < 2:
            head += 1
            print 'Attempt #', counter+1, ": Throwing a coin... It's a head! ... Got ", head, "head(s) so far and ", tail, "tail(s) so far"
        else:
            tail += 1
            print 'Attempt #', counter+1, ": Throwing a coin... It's a tail! ... Got ", tail, "head(s) so far and ", head, "tail(s) so far"

coinToss()