
from math import floor


num_judges = 20
num_projects = 50
projects_per_judge = 6


judge_assignments = []
step_size = (num_projects) / float(num_judges)
curr_start = float(1)

for i in range(num_judges):
    range_start = int(floor(curr_start))
    range_end = range_start + projects_per_judge
    judge_assignments.append([n for n in range(range_start, range_end)])
    curr_start += step_size


for i in range(len(judge_assignments)):
    for j in range(len(judge_assignments[i])):
        if judge_assignments[i][j] > num_projects:
            judge_assignments[i][j] -= num_projects

for assign in judge_assignments:
    print(assign)
