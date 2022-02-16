"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
#import a1_my_queue


class PriorityQueue:
    def __init__(self):
        self.__priority_queue = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }

    def str(self):
        return self.__priority_queue

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.__priority_queue[priority].append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        # if not self.__priority_queue:
        #     return None
        for i in range(10):
            if len(self.__priority_queue[i]) > 0:
                return self.__priority_queue[i].pop(0)
        return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.__priority_queue.clear()
        return None


# a = PriorityQueue()
# a.enqueue("345", 0)
# a.enqueue("234", 1)
# a.enqueue("123", 0)
# print(a.dequeue())
# print(a.dequeue())
# print(a.dequeue())
#print(a)