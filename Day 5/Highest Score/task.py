student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam=sum(student_scores)
print(total_exam)

max=student_scores[0]
for i in range(0,len(student_scores)):
    if student_scores[i]>max:
        max=student_scores[i]

print(f"The highest score in class is: {max}")