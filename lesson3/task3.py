def max_sum(term_list):
    term_list.sort()
    result = term_list[-1] + term_list[-2]
    return result

print (max_sum([9, 0, 10]))