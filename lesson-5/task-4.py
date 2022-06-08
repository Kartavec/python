import os
from conf import OUT_PATH

replace_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
in_file = open(os.path.join(OUT_PATH, 'task-4_in.txt'), 'r')
out_file = open(os.path.join(OUT_PATH, 'task-4_out.txt'), 'w')
out_file.flush()
for line in in_file:
    for search_str, rpl_str in replace_dict.items():
        line = line.replace(search_str, rpl_str)
    out_file.write(line)
in_file.close()
out_file.close()
