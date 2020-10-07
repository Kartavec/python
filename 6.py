import re
ret_dict = dict()
with open('6.txt', 'r') as f:
    for line in f:
        name = line.split()[0]
        nums = re.findall(r'\d+', line)
        nums = [int(i) for i in nums]
        ret_dict[name] = sum(nums)
        # print(f'{name}: {sum(nums)}')

print(ret_dict)