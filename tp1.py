import random

"""part1:listes"""
# generate a list of random numbers 
def generate_list(min=0,max=10,count=10):
    numList = []
    for i in range(0,count):
        n = random.randrange(min,max)
        numList.append(n)
    return numList
 
# generate a set from a list without duplication
def unique(list=[]):
    return set(list) 

# check duplicates
def check_duplicates(list=[]):
    if(len(list)!=len(set(list))):
        print("contains duplicates")
    else:
        print("no duplicates")
        
# generate a set from a list "only duplicated numbers"
def get_duplicates(list=[]):
    duplicate = []
    nonDuplicate = []
    for i in list:
        if i not in nonDuplicate:
            nonDuplicate.append(i)
        else:
            duplicate.append(i)
    return set(duplicate)
    
"""part2:dictionnaires"""

# int list to string list
def toString(list=[]):
    strList = []
    for i in list:
        strList.append(str(i))
    return strList

# even or odd
def even(list=[]):
    pList = []
    for i in list:
        if (i%2) == 0:
            pList.append(True)
        else:
            pList.append(False)
    return pList

# duplicated or not
def duplicated(list=[]):
    dList = []
    nonDuplicate = []
    dup = []
    for i in list:
        if i not in nonDuplicate:
            nonDuplicate.append(i)
        else:
            dup.append(i)
    for i in list:
        if i in dup:
             dList.append(True)
        else:
             dList.append(False)
    return dList

# generate a list of dicts
def generate_dict(list=[]):
    myUniq = unique(list)
    myDup = get_duplicates(list)
    myL = []

    for i in myUniq:
        dict = {
            'number':i,
            'string':str(i),
            'even':(i%2==0),
            'duplicated':i in myDup
        }
        myL.append(dict)
    return myL

# number of odd and duplicated elements
def count_odd_duplicated(list=[]):
    count = 0
    for i in list:
        if (i['even'] == False) and (i['duplicated'] == True):
            count=count+1
    return count

# Testing
myList = []
# test part1
myList = generate_list(0,10,5)
print(myList)
# print(unique(myList))
# check_duplicates(myList)
# print(get_duplicates(myList))

# test part2
myStr = toString(myList)
pair = even(myList)
dup = duplicated(myList)

# print(len(myList))
# myDict = {'Number':myList[0],'string':myStr[0],'even':pair[0],'duplicated':dup[0]}
# print(myDict)
myDict = generate_dict(myList)
print(myDict)
print(count_odd_duplicated(myDict))


