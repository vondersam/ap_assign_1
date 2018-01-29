from timeit import default_timer as timer
from math import log

dict1 = {}
dict2 = []

with open('dict1.txt') as f:
    count = 0
    for line in f: 
        dict1[line.strip()] = count
        count += 1

with open('dict2.txt', 'r') as f:
    for line in f:
        dict2.append(line.strip())
                   
def dict_search(dictionary,word):
    if word in dictionary:
        return dictionary[word]
    return -1

def test_dict():
    results=[]
    for _ in range(25):
        start = timer()
        for key in dict2:
            dict_search(dict1,key)
        end = timer()
        results.append(end - start)
    print(sum(results)/25)

test_dict()





