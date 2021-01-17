#641. Design Circular Deque

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.t = deque()
        self.size = k


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.t.appendleft(value)
            return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.t.append(value)
            return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.t.popleft()
            return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.t.pop()
            return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.t[0]

        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.t[-1]

        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.t) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """

        return len(self.t)== self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
