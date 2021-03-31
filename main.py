from months import Months
from places import Places
from sweepstakes import SweepStakes
from myFamily import MyFamily
from linkedlist import LinkedList
from node import BinarySearchTree
from node import Node

if __name__ == '__main__':

    pi_day = Months().find_month_of_pi()
    places = Places()
    places.print_birthday_places()
    winner = SweepStakes().pick_Winner()
    myFamily = MyFamily()
    print(myFamily)
    linked_list = LinkedList()
    linked_list.append_node(55)
    linked_list.append_node(68)
    linked_list.append_node(65)
    linked_list.prepend_node(0)
    has = linked_list.contains(0)
    print(has)
    bst = BinarySearchTree()
    bst = linked_list.copy_list()
    print(bst.find(55))