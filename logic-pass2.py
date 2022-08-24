def myfunc(mylist, mylist2):
    for item in mylist:
        if mylist.count(item) > 1 and item not in mylist2:
            mylist2.append(item)
    return mylist2
    
    
print(myfunc([1,2,3,4,4,2],[]))
