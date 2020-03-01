
from math import floor


num_judges = 20
num_projects = 50
projects_per_judge = 3


judge_assignments = []
step_size = (num_projects - projects_per_judge) / float(num_judges)
curr_start = float(0)

for i in range(num_judges):
    range_start = int(floor(curr_start))
    range_end = range_start + projects_per_judge
    judge_assignments.append([n for n in range(range_start, range_end)])
    curr_start += step_size


for j in judge_assignments:
    print(j)
