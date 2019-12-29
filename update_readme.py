import time
import glob
import os
import itertools


def get_create_time(path):
	ctime = os.path.getctime(path)
	ctime = time.localtime(ctime)
	return time.strftime('%Y-%m-%d')


def get_question_num_and_name(path):
	lst = path.split('-')
	return lst[0][-4:], '-'.join(lst[1:])[:-3]


solutions = glob.glob('./problems/*.py')
solutions_with_time = [(s, get_create_time(s)) for s in solutions]
solutions_by_date = itertools.groupby(solutions_with_time, key=lambda x: x[1])

output = ''
for dt, solutions in solutions_by_date:
	output += '#### ' + dt + '\n'
	for s, _ in solutions:
		output += '  - ' + get_question_num_and_name(s)[1] + '\n'

with open('README.md', 'w') as f:
	f.write(output)

