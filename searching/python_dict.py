from timeit import default_timer as timer
from math import log

dict1 = {}
dict2 = {}

with open('dict1.txt') as f:
    count = 0
    for line in f: 
        dict1[line.strip()] = count
        count += 1

with open('dict2.txt') as f:
    count = 0
    for line in f: 
        dict2[line.strip()] = count
        count += 1  
'''
def seq_search(dictionary, word):
    for element in dictionary:
        if element == word:
            return dictionary[element]
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
'''

def dict_search(dictionary,word):
        if word in dictionary:
            return dictionary[word]
        return -1

start = timer()
for key in dict2:
    dict_search(dict1,key)
end = timer()
print(end - start)


'''
print("RESULTS FOR SEQUENCIAL")
start = timer()
for key in dict2:
    seq_search(dict1, key)
end = timer()
print(end - start)
#Best result for sequencial so far: 44.495771093061194

print("RESULTS FOR BINARY")
start = timer()
for key in dict2:       
    bi_search(dict1, key)
end = timer()
print(end - start)
#Best result for binary so far: 0.1990395630709827
'''





