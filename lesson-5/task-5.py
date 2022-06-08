import os
import random
import conf

out_file = os.path.join(conf.OUT_PATH, 'task-5.txt')
# generate file with nums
with open(out_file, 'w') as f:
    f.write(' '.join(map(str, random.sample(range(0, 100), random.randint(10, 40)))))

with open(out_file, 'r') as f:
    print('Sum:', end=' ')
    print(sum(map(int, f.readline().split())))
