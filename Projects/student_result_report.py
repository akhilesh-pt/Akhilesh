college_name = "ABC College Of Advanced Studies"
student_result_report = "STUDENT RESULT REPORT"
student_1_name = input("Enter student 1 name : ")
student_1_id = input("Enter student 1 id : ")
student_1_english_marks = int(input("Enter student 1 english marks : "))
student_1_mathematics_marks = int(input("Enter student 1 mathematics marks : "))
student_1_science_marks = int(input("Enter student 1 science marks : "))
student_1_it_marks = int(input("Enter student 1 IT marks : "))
student_1_total = student_1_english_marks + student_1_mathematics_marks + student_1_science_marks + student_1_it_marks

student_1_average = student_1_total / 4

print()
print("===============================================================================")
print(college_name.center(60))
print("===============================================================================")
print()
print("-------------------------------------------------------------------------------")
print(student_result_report.center(60))
print("-------------------------------------------------------------------------------")

print()
print(f"{"Student name":20} : {student_1_name}")
print(f"{"Student ID":20} : {student_1_id}")

print()
print("-------------------------------------------------------------------------------") 
print()    
print(f"{"English Marks":20} : {student_1_english_marks}")
print(f"{"Mathematics Marks":20} : {student_1_mathematics_marks}")
print(F"{"science Marks":20} : {student_1_science_marks}")
print(f"{"IT Marks":20} : {student_1_it_marks}")
print()
print(f"{"Total Marks":20} : {student_1_total}")
print(f"{"Average Marks":20} : {student_1_average}")
print()
print("-------------------------------------------------------------------------------")
if student_1_average >= 90:
    student_1_grade = "A+"
elif student_1_average >= 80:
    student_1_grade = "A"
elif student_1_average >= 70:
    student_1_grade = "B+"
elif student_1_average >= 60:
    student_1_grade = "B"
else:
    student_1_grade = "C"
print()
print(f"{"Grade" :20} : {student_1_grade}")

if student_1_average >= 90:
    student_1_assessment = "Excellent"
elif student_1_average >= 80:
    student_1_assessment = "Very Good"
elif student_1_average >= 70:
    student_1_assessment = "Good"
elif student_1_average >= 60:
    student_1_assessment = "OK"
else:
    student_1_assessment = "Need Improvement"
print(f"{"Student Assessment":20} : {student_1_assessment}")

print()
print("===============================================================================")
