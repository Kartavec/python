

def more_then_next(inp_list):
    for i in range(1, len(inp_list)):
        if inp_list[i] > inp_list[i - 1]:
            yield inp_list[i]


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(list(more_then_next(my_list)))
