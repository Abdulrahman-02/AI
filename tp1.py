import random

# generate a list of random numbers 
def generate_list(min=0,max=10,count=10):
    numList = []
    for i in range(0,count):
        n = random.randrange(min,max)
        numList.append(n)
    return numList
 
# generate a set from a list without duplication
def unique(list=[]):
    mySet = {}
    mySet = set(list)
    return mySet 

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

# Testing
myList = []
myList = generate_list(0,10,15)
print(myList)
print(unique(myList))
check_duplicates(myList)
print(get_duplicates(myList))


