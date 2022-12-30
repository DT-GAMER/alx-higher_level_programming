def safe_print_list(my_list=[], x=0):
    print_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
            print("")
        except IndexError:
            break
    print("")
    return (printed_elements)

