def compareLists (list1, list2):
    if cmp(list1, list2) != 0:
        print 'The lists are not the same'
    else:
        print 'The lists are identical'
    # if len(list1) != len(list2):
    #     print 'The lists are not the same'
    # else:
    #     for index in range (0, len(list1)):
    #         if list1[index]!=list2[index]:
    #             print 'The lists are not the same'
    #             break
    #     else:
    #         print 'The lists are identical'

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_one1 = [1,2,5,6,5]
list_two2 = [1,2,5,6,5,3]
list_one11 = [1,2,5,6,5,16]
list_two22 = [1,2,5,6,5]
list_one111 = ['celery','carrots','bread','milk']
list_two222 = ['celery','carrots','bread','cream']

compareLists (list_one, list_two)
compareLists (list_one1, list_two2)
compareLists (list_one11, list_two22)
compareLists (list_one111, list_two222)