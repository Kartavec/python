import os
import conf

try:
    with open(os.path.join(conf.OUT_PATH, 'task-2.txt'), 'r') as f:
        file_lines = f.readlines()
        print(f'Lines: %s' % (len(file_lines)))
        for i, v in enumerate(file_lines):
            print('Words in line#%s: %s' % ((i + 1), len(v.split())))
except IOError:
    print('File not exists')
