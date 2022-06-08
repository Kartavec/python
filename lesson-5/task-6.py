import os
import re
import conf

result = {}
try:
    with open(os.path.join(conf.OUT_PATH, 'task-6.txt')) as f:
        for line in f:
            line_split = line.split()
            result[line_split[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(result)
except IOError:
    print('File not exists')
