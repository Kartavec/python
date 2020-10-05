
def list_to_unique(inp_list):
    for i in range(len(inp_list)):
        if not inp_list[i] in inp_list[:i] + inp_list[i + 1:]:
            yield inp_list[i]


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(list(list_to_unique(my_list)))

