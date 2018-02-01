class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        self.freq = 1

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def getFreq(self):
        return self.freq

    def setNext(self,newnext):
        self.next = newnext

    def addFreq(self):
        self.freq += 1



class FreqLinkedList:
    def __init__(self):
        self.head = Node("**dummy**", None)

    def search(self,word):
        current = self.head
        found = False
        found_word = None
        while current != None and not found:
            if current.getData() == word:
                found = True
                found_word = current
            else:
                current = current.getNext()
        return found_word
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    
    def addWord(self, word):
        if self.search(word) != None:
            self.search(word).addFreq()
        else:
            currentNode = Node(word, self.head)
            nextNode = currentNode.getNext()
            previousNode = None
            bigger = True
            while nextNode != None and bigger:
                if word < nextNode.getData():
                    previousNode = nextNode#pizza
                    nextNode = nextNode.getNext()#ajar
                else:
                    if previousNode == None:
                        currentNode.setNext(nextNode)
                        self.head = currentNode
                        bigger = False
                    else:
                        tempnext = nextNode
                        temp = previousNode
                        temp.setNext(currentNode)
                        currentNode.setNext(tempnext)
                        bigger = False

    def remove(self,word):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == word:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
                        
    def filterWords(self,n):
        current = self.head
        while current != None:
            if current.getFreq() < n:
                self.remove(current.getData())
            current = current.getNext()
        
      
    def printList(self):
        current = self.head
        while current != None:
            print(str(current.getData()), str(current.getFreq()))
            current = current.getNext()


d = FreqLinkedList()

d.addWord("ajar")
d.addWord("pizza")
d.addWord("car")
d.addWord("car")
d.addWord("car")
d.addWord("car")
d.addWord("bar")
d.addWord("car")
d.addWord("car")
d.addWord("car")
d.addWord("bar")
d.addWord("car")
d.addWord("car")
d.addWord("car")
d.addWord("bar")
d.addWord("car")
d.addWord("car")
d.addWord("car")
d.addWord("bar")
d.addWord("car")
d.addWord("car")
d.addWord("car")
d.addWord("bar")
d.addWord("zebra")
d.addWord("woho")
d.addWord("zasca")
d.addWord("pizza")
d.addWord("pizza")

d.printList()

'''
    def alphaOrder(self,word):
        current = [self.head, ""]
        previous = None
        comparator = True
        while current[0] != None or comparator:
            if current[0] != None:
                if word < current[0].getData():
                    if previous == None:
                        current = [current[0], "prefix"]
                        comparator = False
                    else:
                        current = [previous[0], "infix"]
                        comparator = False
                else:
                    previous = current[0]
                    current = [current[0].getNext(), '']
                    comparator = True
            else:
                current = [previous, "prefix"]
                comparator = False
        print(current)
        return current


 def addWord(self, word):
        if self.search(word):
            self.head.addFreq()
        else:
            if self.size() < 2:
                self.head = Node(word, self.head)
            else:
                nextNode = self.head.getNext()
                self.head = Node(word, self.head)
                previousNode = None
                bigger = True
                while nextNode != None and not bigger:
                    if self.head.getData() > nextNode.getData():
                        previousNode = nextNode
                        nextNode = nextNode.getNext()
                    else:
                        if previousNode == None:
                            self.head.setNext(nextNode)
                            bigger = False
                        else:
                            self.head.setNext(nextNode)
                            previous.setNext(self.head)
                            bigger = False

'''
