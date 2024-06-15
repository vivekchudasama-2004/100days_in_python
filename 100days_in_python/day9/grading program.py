student_scores={
    "Harry": 81,
    "Ron": 78,
    "Hermit": 76,
    "draco": 74,
    "neville": 62
}
#creating empty dictonary
student_grades={}

#adding grad in student_scors
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="oustanding"
    elif score>80:
        student_grades[student]="exceed expection"
    elif score>70:
        student_grades[student]="acceptable"
    else:
        student_grades[student]="fail"
print(student_grades)