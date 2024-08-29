"""
A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over.
"""

sweet_total = int(input("How many sweets are in the container? "))
student_total = int(input("How many pupils attended today? "))

sweet_loss = sweet_total / student_total
sweet_total = sweet_total - sweet_loss

print(f"There should be {sweet_loss} sweets distributed today, with {sweet_total} left over at the end of the day.")

exit(0)