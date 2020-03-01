import csv
import sys


# Default values and hard-coded hacks 👀
DEFALUT_NAME = "file.csv"
OUTPUT_CSV_NAME = "aggregated_data.csv"
OUTPUT_CSV_DICT = {}

project_number_index = 2
scoring_indices = (4,8)

#new col: num judges, total score (avg)

# Read file name from input if it's there
file_name = DEFALUT_NAME
file_arg = sys.stdin
if type(file_arg) == str:
    file_name = file_arg


# Reading from file, adding column to output csv with total scores
with open(file_name,"r") as fdsc_in, open(OUTPUT_CSV_NAME,"w+") as fdsc_out:
    file_lines = fdsc_in.read().split('\n')
    csv_writer = csv.writer(fdsc_out,delimiter=',')

    nasty_thing = ["num judges", "total score (avg)"] + [value.replace('"','') for value in file_lines[0].split(",")]
    print(nasty_thing)
    csv_writer.writerow(nasty_thing)

    for entry in file_lines[1:-1]:
        entry_list = [value.replace('"','') for value in entry.split(",")]
        score_sum = 0
        for value in entry_list[scoring_indices[0]:scoring_indices[1]]:
            score_sum += int(value.replace('"',''))

        if entry_list[project_number_index] not in OUTPUT_CSV_DICT:
            OUTPUT_CSV_DICT[entry_list[project_number_index]] = (score_sum, 1, entry_list)
        else:
            curr_score = OUTPUT_CSV_DICT[entry_list[project_number_index]][0]
            curr_judges = OUTPUT_CSV_DICT[entry_list[project_number_index]][1]
            new_score = ((curr_score*curr_judges) + score_sum)/(curr_judges+1)
            OUTPUT_CSV_DICT[entry_list[project_number_index]] = (new_score, curr_judges + 1, entry_list)

    for k,v in OUTPUT_CSV_DICT.items():
        output_row = [v[1]] + [v[0]] + v[2]
        print(output_row)
        csv_writer.writerow(output_row)
