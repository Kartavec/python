def fact():
    n = 4

    fact_list = [el for el in range(1, n + 1)]
    print(fact_list)
    from functools import reduce
    def my_func(prev_el, el):
        return prev_el * el
        print(reduce(my_func, fact_list))
        yield reduce(my_func, fact_list)
c = fact()
print(c)


