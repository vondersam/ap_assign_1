from timeit import default_timer as timer
from math import log
from random import shuffle


li = []
li2 = []

with open('dict1.txt') as f: 
    for line in f: 
        li.append(line.strip()) 

with open('dict2.txt') as f:
    for line in f:
        li2.append(line.strip())

shuffle(li2)
 
dict2_10 = sorted(li2[:10])
dict2_100 = sorted(li2[:100])
dict2_1000 = sorted(li2[:1000])
dict2_10000 = sorted(li2[:10000])
li2.sort()

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



dictionaries = [dict2_10, dict2_100, dict2_1000, dict2_10000]

'''
def test_seq():
    for dix in dictionaries:
        results=[]
        for _ in range(25):
            start = timer()
            for key in dix:
                seq_search(li, key)
            end = timer()
            results.append(end - start)
        print("25 times sequential search for", len(dix), "words took:", sum(results)/25, "seconds")


test_seq()



def test_bi():
    for dix in dictionaries:
        results=[]
        for _ in range(25):
            start = timer()
            for key in dix:
                bi_search(li, key)
            end = timer()
            results.append(end - start)
        print("25 times binary search for", len(dix), "words took:", sum(results)/25, "seconds")

test_bi()

SEQUENTIAL

0.0198494 

0.1768789 

1.6496573

16.5818150

BINARY

0.0000467

0.0004678

0.0045199 

0.0450594 
'''
