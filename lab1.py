
def removeDuplicates(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist


def sortList(mylist):
    mylist.sort()
    return mylist

a_dict= {"a":10, "b":12, "c":14, "d":14, "e":16, "f":28, "g":28, "h":30}
a_dict = removeDuplicates(a_dict)
print(a_dict)

a_dict = sortList(a_dict)
print(a_dict)