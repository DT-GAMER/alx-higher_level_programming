#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        printed_elements = 0
        for i in range (x):
            print(my_list[i], end=' ')
            printed_elements += 1
            print()
    except indexerror:
        pass
    print()
    return printed_elements

        
