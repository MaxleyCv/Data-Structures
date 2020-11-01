from structures import *

INPUT_FILE = open("input.txt", "r")


def find_best_price(items_list, discount):
    """
    :param items_list: dequeue with prices
    :param discount: discount on each third product
    :return: minimum price to pay
    >>> items = Dequeue()
    >>> for item in [1, 2, 98, 97]: items.add(item)
    >>> find_best_price(items, 20)
    178.4
    >>> items = Dequeue()
    >>> for item in [20, 20, 100, 90, 80, 60, 70, 50]: items.add(item)
    >>> find_best_price(items, 20)
    452.0
    """
    tree = Tree()

    for items_count in range(items_list.length):
        tree.add_element(items_list.pop_last())

    tree.lnr_search(items_list)

    discount /= 100
    discount = 1 - discount
    to_pay = 0
    item_position = 0

    for items_count in range(items_list.length):
        if item_position != 2:
            to_pay += items_list.pop_first()
        else:
            to_pay += discount * items_list.pop_last()
            item_position = -1
        item_position += 1

    return to_pay


if __name__ == '__main__':
    items_list = Dequeue()
    for element in list(map(int, INPUT_FILE.readline().split(' '))):
        items_list.add(element)
    discount = int(INPUT_FILE.readline())
    print(find_best_price(items_list, discount))
