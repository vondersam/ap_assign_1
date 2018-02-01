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
        self.head = Node("å**dummy**", None)

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
                if word > nextNode.getData():
                    previousNode = nextNode
                    nextNode = nextNode.getNext()
                else:
                    if previousNode == None:
                        currentNode.setNext(nextNode)
                        self.head = currentNode
                        bigger = False
                    else:
                        temprev = previousNode
                        temp = nextNode
                        temprev.setNext(currentNode)
                        currentNode.setNext(temp)
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



