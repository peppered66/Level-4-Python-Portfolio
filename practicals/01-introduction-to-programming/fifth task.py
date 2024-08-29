"""
The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is 24 students, since this is the
number of PCs in a lab. Write a program that calculates how many groups are
needed for the following number of students: 113, 175, 12. Display how many full
groups there will be, and how many students will be in the smaller "left over"
group.
"""
total_students = 300
group_size = 24

total_groups = total_students / group_size
total_groups = int(total_groups)

small_group = total_students - (total_groups * group_size)

print(f"""
The total amount of full size groups of 24 students for this year are {total_groups}. With a smaller
group of {small_group} students.
""")