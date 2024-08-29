#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    import csv
    our_cat = 0
    other_cat = 0
    visits = []

    if len(sys.argv) < 2:
        print("Please enter a log to inspect.")
        exit()

    with open(sys.argv[1], 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == 'THEIRS':
                other_cat +=1

            elif row[0] == 'OURS':
                our_cat +=1
                enter_time = row[1]
                exit_time = row[2]
                visit_time = int(exit_time) - int(enter_time)
                visits.append(visit_time)

    total_time = sum(visits)
    longest_visit = max(visits)
    shortest_visit = min(visits)
    average_visit = sum(visits) // len(visits)
    print("Log file analysis.")
    print("Cat visits:", our_cat)
    print("Other cat visits", other_cat)
    print("Total time in house:", total_time // 60, "hours,", total_time % 60, "minutes")
    print("Average visit length:", average_visit // 60, "hours,", average_visit % 60, "minutes")
    print("Longest visit:", longest_visit // 60, "hours,", longest_visit % 60, "minutes")
    print("Shortest visit:", shortest_visit // 60, "hours,", shortest_visit % 60, "minutes")
