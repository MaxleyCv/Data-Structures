from structures import *


if __name__ == '__main__':
    items_list = Dequeue()
    for element in list(map(int, input().split(' '))):
        items_list.add(element)
    discount = int(input())
    tree = Tree()

    for items_count in range(items_list.length):
        tree.add_element(items_list.pop_last())

    tree.get_elements(items_list)

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
    
    print(to_pay)

