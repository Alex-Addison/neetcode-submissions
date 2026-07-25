class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        currNode = self.head
        while currNode and currNode.next and index > 0:
            currNode = currNode.next
            index-=1
        if index > 0 or currNode == None:
            return -1
        return currNode.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head)
        self.head = newNode

    def insertTail(self, val: int) -> None:
        print(self.getValues())
        currNode = self.head
        prevNode = None
        while currNode:
            prevNode = currNode
            currNode = currNode.next
        if prevNode:
            prevNode.next = Node(val)
        else:
            self.head = Node(val)

    def remove(self, index: int) -> bool:
        currNode = self.head
        prevNode = None
        while currNode and currNode.next and index > 0:
            prevNode = currNode
            currNode = currNode.next
            index-=1
        if index > 0 or currNode == None:
            return False
        if prevNode:
            prevNode.next = currNode.next
        else:
            self.head = self.head.next if self.head else None
        return True

    def getValues(self) -> List[int]:
        arr = []
        currNode = self.head
        while currNode:
            arr.append(currNode.val)
            currNode = currNode.next
        return arr
