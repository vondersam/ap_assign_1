from timeit import default_timer as timer
from collections import deque
from math import log

li = deque()
li2 = []

with open('dict1.txt') as f: 
    for line in f: 
        li.append(line.strip()) 

with open('dict2.txt') as f:
    for line in f:
        li2.append(line.strip()) 

def seq_search(dictionary, word):
    count = 0
    for element in dictionary:
        if element == word:
            return count
        count += 1
    return -1

def bi_search(dictionary, word):
    first = 0                                
    last = (len(dictionary)-1)               
    logn = int(log(last,2))                  
    for i in range(logn):
        midpoint = (first + last) // 2
        if dictionary[midpoint] == word:
            return midpoint                 
        else:
            if word < dictionary[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1     
    return -1                            



print("RESULTS FOR SEQUENCIAL")
def test_seq():
    results=[]
    for _ in range(25):
        start = timer()
        for key in li2:
            seq_search(li, key)
        end = timer()
        results.append(end - start)
    print(sum(results)/25)


test_seq()
'''


print("RESULTS FOR BINARY")
def test_bi():
    results=[]
    for _ in range(25):
        start = timer()
        for key in li2:
            bi_search(li, key)
        end = timer()
        results.append(end - start)
    print(sum(results)/25)

test_bi()

'''
