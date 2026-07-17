student_result_report = "STUDENT RESULT REPORT"
student_name = input("Enter student name : ")
student_id = input("Enter student id : ")
english_marks = int(input("Enter english marks : "))
mathematics_marks = int(input("Enter mathematics marks : "))
science_marks = int(input("Enter science marks : "))
total_marks = english_marks + mathematics_marks + science_marks
average_marks = total_marks / 3

print("\n============================================================")
print(student_result_report.center(60))
print("==============================================================")

print("\nStudent Name           : ",student_name)
print("Student ID               : ",student_id)

print("\nEnglish Marks          : ",english_marks)
print("Mathematics Marks        : ",mathematics_marks)
print("Science Marks            : ",science_marks)

print("--------------------------------------------------------------")

print("\nTotal Marks            : ",total_marks)
print("Average Marks            : ",average_marks)

print("\n------------------------------------------------------------")
if average_marks >= 50:
    print("Result               : PASS")
else:
    print("Result               : FAIL")

if average_marks >= 50:
        print("CONGRATULATIONS")
else:
     print("BETTER LUCK NEXT TIME")


print("==============================================================")
