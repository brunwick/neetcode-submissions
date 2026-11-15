class MyLinkedList:
    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


    def __init__(self):
        self.dummy = self.Node()


    def get(self, index: int) -> int:
        if not self.dummy:
            return -1
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1
        return curr.next.val if curr.next else -1


    def addAtHead(self, val: int) -> None:
        self.dummy.next = self.Node(val=val, next=self.dummy.next)


    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = self.Node(val=val)


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
            if not curr:
                return
        curr.next = self.Node(val=val, next=curr.next)
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
            if not curr:
                return
        if curr.next:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)