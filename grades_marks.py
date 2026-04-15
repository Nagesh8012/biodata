##marks=float(input("Enter your marks:"))
##
##if marks>=90:
##    grade="A+"
##elif  marks>=80:
##    grade="A"
##elif  marks>=70:
##    grade="B+"
##elif  marks>=60:
##    grade="B"
##elif  marks>=50:
##    grade="C"
##elif  marks>=40:
##    grade="D"
##else:
##    grade="F"
##print("Your Grade is:",grade)


#using functions

def calculate_grade(marks):
    if marks>=90:
        return"A+"
    elif  marks>=80:
        return"A"
    elif  marks>=70:
        return"B+"
    elif  marks>=60:
        return"B"
    elif  marks>=50:
        return"C"
    elif  marks>=40:
        return"D"
    else:
        return"F"

#main program
marks=float(input("Enter marks:"))
grade=calculate_grade(marks)
print("Grades=",grade)



