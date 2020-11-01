import copy


class TreeNode:
    """
    Binary Tree node class
    """
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """
    class for implementation of binary trees
    """
    def __init__(self):
        self.root = None

    @staticmethod
    def append(node, val):
        """
        :param node: node of the tree
        :param val: value to append
        :return: none
        """
        if val < node.val:
            if node.left:
                Tree.append(node.left, val)
            else:
                node.left = TreeNode(val, None, None)
        else:
            if node.right:
                Tree.append(node.right, val)
            else:
                node.right = TreeNode(val, None, None)

    def add_element(self, val):
        """
        :param val: value to add to the binary tree
        :return: none
        """
        if not self.root:
            self.root = TreeNode(val, None, None)
        else:
            Tree.append(self.root, val)

    @staticmethod
    def nuclear_lnr_search(node, result):
        """
        LNR node getting method
        :param node: node of the tree
        :param result: deque to append the values
        :return: none
        """
        if node.left:
            Tree.nuclear_lnr_search(node.left, result)
        result.add(node.val)
        if node.right:
            Tree.nuclear_lnr_search(node.right, result)

    def lnr_search(self, result):
        """
        :param result: deque which will contain sorted elements after lnr coming
        :return: sorted deque with elements
        >>> A = Dequeue()
        >>> T = Tree()
        >>> for i in [87, 32, 11]: T.add_element(i)
        >>> A = T.lnr_search(A)
        >>> A.pop_first()
        11
        >>> A.pop_last()
        87
        """
        Tree.nuclear_lnr_search(self.root, result)
        return result


class DeqNode:
    """
    Node of dequeue class
    """
    def __init__(self, next, previous, val):
        self.next = copy.deepcopy(next)
        self.previous = copy.deepcopy(previous)
        self.val = val


class Dequeue:
    """
    A data structure deque class
    possible to add element, get first or last
    """

    def __init__(self):
        self.first = DeqNode(None, None, None)
        self.last = DeqNode(None, None, None)
        self.length = 0

    def add(self, val):
        """
        method to append the element to dequeue
        :param val: value to append
        :return: none
        >>> A = Dequeue()
        >>> A.add(3)
        >>> A.first.val
        3
        >>> A.last.val
        3
        """
        if self.length == 0:
            self.first = copy.deepcopy(DeqNode(None, None, val))
            self.last = copy.deepcopy(DeqNode(None, None, val))
        elif self.length == 1:
            self.last.next = DeqNode(None, self.first, val)
            self.last = copy.deepcopy(DeqNode(None, self.first, val))
            self.first.next = self.last
            self.last.previous = self.first
        else:
            self.last.next = copy.deepcopy(DeqNode(None, self.last, val))
            self.last = self.last.next
        self.length += 1

    def pop_first(self):
        """
        Method to get the first element of dequeue
        :return: first element of dequeue or none if not exists
        >>> A = Dequeue()
        >>> A.add(4)
        >>> A.add(5)
        >>> A.pop_first()
        4
        >>> A.pop_first()
        5
        """
        if self.length:
            element = copy.deepcopy(self.first)
            if self.length != 1:
                self.first = self.first.next
            self.first.previous = None
            self.length -= 1
            return element.val
        else:
            return None

    def pop_last(self):
        """
        Method to get the first element of dequeue
        :return: last element of dequeue or none if not exists

        >>> D = Dequeue()
        >>> D.add(4)
        >>> D.add(5)
        >>> D.add(6)
        >>> D.pop_last()
        6
        >>> D.add(8)
        >>> D.pop_last()
        8
        >>> D.pop_last()
        5
        """
        if self.length:
            element = copy.deepcopy(self.last)
            if self.last.previous:
                self.last = self.last.previous
            if self.last:
                self.last.next = None
            self.length -= 1
            return element.val
        else:
            return None

