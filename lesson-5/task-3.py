import os
import conf

try:
    salary_list = []
    with open(os.path.join(conf.OUT_PATH, 'task-3.txt'), 'r') as f:
        for line in f:
            try:
                line_split = line.split()
                salary = float(line_split[1])
                salary_list.append(salary)
                if salary < 20000:
                    print(line_split[0])
            except TypeError:
                print('Line parse error. %s' % line)
            except IndexError:
                print('Line parse error. %s' % line)

    print('Average salary: %.2f' % (sum(salary_list)/len(salary_list)))
except IOError:
    print('File not exists')
