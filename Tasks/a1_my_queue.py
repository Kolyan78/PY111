"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.__my_queue = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.__my_queue.append(elem) # O(1)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.__my_queue:
            return None
        return self.__my_queue.pop(0) # O(1)


    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        if ind >= len(self.__my_queue): # O(1)
            return None

        return self.__my_queue[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.__my_queue.clear() # O(1)
        return None
