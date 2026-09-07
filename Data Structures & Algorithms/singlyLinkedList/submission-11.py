class Listval:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Listval(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Listval(val, self.head.next)
        self.head.next = new_node
        if self.tail == self.head:
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.tail.next = Listval(val)
        self.tail = self.tail.next
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        i = 0
        curr = self.head
        while i < index and curr.next:
            i += 1
            curr = curr.next

        if curr and curr.next and i == index:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            self.size -= 1  # Decrement size
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
