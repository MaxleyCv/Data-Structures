import copy


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    @staticmethod
    def append_left(node, val):
        if val < node.val:
            if node.left:
                Tree.append_left(node.left, val)
            else:
                node.left = TreeNode(val, None, None)
        else:
            if node.right:
                Tree.append_left(node.right, val)
            else:
                node.right = TreeNode(val, None, None)

    def add_element(self, val):
        if not self.root:
            self.root = TreeNode(val, None, None)
        else:
            Tree.append_left(self.root, val)

    @staticmethod
    def get(node, result):
        if node.left:
            Tree.get(node.left, result)
        result.add(node.val)
        if node.right:
            Tree.get(node.right, result)

    def get_elements(self, result):
        Tree.get(self.root, result)
        return result


class DeqNode:
    def __init__(self, next, previous, val):
        self.next = copy.deepcopy(next)
        self.previous = copy.deepcopy(previous)
        self.val = val


class Dequeue:
    def __init__(self):
        self.first = DeqNode(None, None, None)
        self.last = DeqNode(None, None, None)
        self.length = 0

    def add(self, val):
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

