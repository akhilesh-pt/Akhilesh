salary_slip = "SALARY SLIP"
name = input("Enter name : ")
employee_id = input("Enter employee id: ")
attendance = int(input("Enter attendance : "))
hours = int(input("Enter hours : "))
basic_salary = int(input("Enter basic salary : "))
if attendance >= 25:
    attendance_bonus = 2500
else:
    attendance_bonus = 0
if hours >= 200:
    hours_bonus = 2000
else:
    hours_bonus = 0
if basic_salary >= 25000:
    tax = 0.12
else:
    tax = 0.09
if basic_salary >= 25000:
    insurance = 0.06
else:
    insurance = 0.04

gross_salary = basic_salary + attendance_bonus + hours_bonus
tax_amount = gross_salary * tax
insurance_amount = gross_salary * insurance
net_salary = gross_salary - tax_amount - insurance_amount

print()
print("======================================================================")
print(salary_slip.center(60))
print("======================================================================")

print()
print(f"{"Employee Name":20} : {name}")
print(f"{"Employee ID":20} : {employee_id}")
print(f"{"Attendance":20} : {attendance:.2f}")
print(f"{"Hours":20} : {hours:.2f}")
print()
print("-----------------------------------------------------------------------")

print()
print(f"{"Attendance":20} : {attendance:.2f}")
print(f"{"Hours":20} : {hours:.2f}")
print(f"{"Basic Salary":20} : {basic_salary:.2f}")
print(f"{"Tax":20} : {tax_amount:.2f}")
print(f"{"Insurance":20} : {insurance_amount:.2f}")
print(f"{"Attendance Bonus":20} : {attendance_bonus:.2f}")
print(f"{"Hours Bonus":20} : {hours_bonus:.2f}")
print(f"{"Gross Salary":20} : {gross_salary:.2f}")
print(f"{"Net Salary":20} : {net_salary:.2f}")
print()
print("======================================================================")