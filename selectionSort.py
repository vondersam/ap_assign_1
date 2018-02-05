from sortarray import *

def selectionSort(sa):
    for i in range(0, sa.getSize()-1):
        min = i
        for j in range(i+1, sa.getSize()):
            if sa.cmp(j,min) < 0:
                min = j
        sa.swap(i,min)

def insertionSort(sa):
    for i in range(1, sa.getSize()):
        position = i
        while position > 0 and sa.cmp(position-1,position) > 0:
            sa.swap(position, position-1)
            position -= 1

def bubbleSort(sa):
    exchanges = True
    passnum = sa.getSize()-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if sa.cmp(i, i+1)>0:
                exchanges = True
                sa.swap(i, i+1)
        passnum -= 1

def shellSort(sa):
    gaps = [701,301,132,57,23,10,4,1]
    for gap in gaps:
        if gap <= sa.getSize():
            for i in range(0, sa.getSize(), gap):
                position = i
                while position > 0 and sa.cmp(position-gap, position) > 0:
                    sa.swap(position, position-gap)
                    position -= gap


debug = False

sa = SortArray()
for size in range(10, 51, 10):
    print ("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print ("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print ("before: ")
            sa.printList()
        
        shellSort(sa) #change me accordingly if you want to see the results for the other methods

        if debug:
            print ("after: ")
            sa.printList()

        sa.printInfo()
    
    print()
