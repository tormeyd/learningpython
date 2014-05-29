#!/usr/bin/python
""" This is nester.py provides one function called print_lol() that prints lists """


def print_lol(the_list):
    """ The function takes a positional arg "the_list" and prints the list, or nested list"""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
             print (each_item)

