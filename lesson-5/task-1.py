import os
import conf

res_file = open(os.path.join(conf.OUT_PATH, 'task-1.txt'), 'w')
while True:
    input_str = input('Enter string (empty for stop): ')
    if len(input_str) == 0:
        break
    res_file.write(input_str)
    res_file.write('\n')

res_file.close()
