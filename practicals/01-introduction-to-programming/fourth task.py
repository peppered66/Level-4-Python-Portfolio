"""In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average.
Note: A batting average is the number of runs scored divided by the number of
completed innings (i.e. the total times batted minus the times not out).
"""

match_total = 609
bat_total = 1014
not_out_total = 162
runs_total = 48426

batting_average = runs_total / (bat_total - not_out_total)
batting_average = round(batting_average, 2)

print(f"The batting average of Geoffrey is {batting_average} which is very impressive!")