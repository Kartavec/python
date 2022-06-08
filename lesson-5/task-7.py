import os
import json
from conf import OUT_PATH

in_file = os.path.join(OUT_PATH, 'task-7.txt')
out_file = os.path.join(OUT_PATH, 'task-7_out.json')
positive_profit = 0
positive_profit_count = 0
firms = {}
try:
    with open(in_file) as f:
        for line in f:
            line_split = line.split()
            prof = float(line_split[2]) - float(line_split[3])
            if prof > 0:
                positive_profit += prof
                positive_profit_count += 1

            firms[line_split[0]] = prof

    with open(out_file, 'w') as f:
        print([firms, {'average_profit': round(positive_profit / positive_profit_count, 2)}])
        f.write(json.dumps([firms, {'average_profit': round(positive_profit / positive_profit_count, 2)}]))
except IOError:
    print('File not exists')
