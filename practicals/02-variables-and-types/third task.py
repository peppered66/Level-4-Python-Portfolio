"""
The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be left over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101
students in groups of 20 the output would be:
There will be 5 groups with 1 student left over
"""

total_students = int(input("How many students are studying this year? "))
group_size = int(input("How many students are required per group? "))

total_groups = total_students / group_size
total_groups = int(total_groups)
small_group = total_students - (total_groups * group_size)

print(f"The total amount of full size groups for this year are {total_groups} with a small group of {small_group} students.")
exit(0)
