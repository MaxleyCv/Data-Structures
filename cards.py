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


class Queue:
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


cards = Queue()
for card in list(map(int, input().split(' '))):
    cards.add(card)

tree = Tree()
for i in range (cards.length):
    tree.add_element(cards.pop_first())

tree.get_elements(cards)

longest_substring = 0
current_substring = 1
previous = cards.pop_first()

for i in range(cards.length):
    current_element = cards.pop_first()
    if current_element - previous <= 1:
        if current_element != previous:
            current_substring += 1
    else:
        if current_substring > longest_substring:
            longest_substring = copy.deepcopy(current_substring)
        current_substring = 1

    if i == cards.length - 2:
        if current_substring > longest_substring:
            longest_substring = copy.deepcopy(current_substring)

    previous = copy.deepcopy(current_element)

print(longest_substring)
