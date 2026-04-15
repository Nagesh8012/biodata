#Python program to find the highest marks from a stident data dictionary
students={
    'Alice':85,
    'Bob':92,
    'Charlie':78,
    'David':90
}

#Find highest marks
highest_marks=max(students.values())
#Find student(s) with highest marks
top_students=[name for name,marks in students.items() if
              marks==highest_marks]
print("Highest Marks:",highest_marks)
print("Top Student(s):",",".join(top_students))
