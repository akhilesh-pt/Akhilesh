company_name = input("Enter comapny name : ")
company_id = input("Enter company id : ")
branch = input("Enter barnch : ")
address = input("Enter address : ")
telephone = input("Enter telephone number : ")
email = input("Enter email : ")
website = input("Enter website : ")

employee_profile_report = "EMPLOYEE PROFILE REPORT"
employee_name_ceo = input("Enter CEO name : ")
employee_id_ceo = input("Enter CEO employee id : ")
designation_ceo = input("Enter designation :")
basic_salary_ceo = int(input("Enter basic salary of CEO : "))
bonus_ceo = int(input("Enter CEO bonus : "))
overtime_ceo = int(input("Enter CEO overtime pay : "))
gross_salary_ceo = basic_salary_ceo + bonus_ceo + overtime_ceo
attendance_ceo = input("Enter CEO attendance % : ")
performance_ceo = input("Enter performnace level of CEO : ")
Status_ceo = input("Enter CEO status : ")

employee_name_md = input("Enter MD name : ")
employee_id_md = input("Enter MD employee id : ")
designation_md = input("Enter designation : ")
basic_salary_md = int(input("Enter basic salary of MD : "))
bonus_md = int(input("Enter MD bonus : "))
overtime_md = int(input("Enter MD overtime pay : "))
gross_salary_md = basic_salary_md + bonus_md + overtime_md
attendance_md = input("Enter MD attendance % : ")
performance_md = input("Enter performance level of MD : ")
status_md = input("Enter MD status : ")

employee_name_om = input("Enter OM name : ")
employee_id_om = input("Enter OM employee id : ")
designation_om = input("Enter designation : ")
basic_salary_om = int(input("Enter basic salary of OM : "))
bonus_om = int(input("Enter OM bonus : "))
overtime_om = int(input("Enter OM overtime pay : "))
gross_salary_om = basic_salary_om + bonus_om + overtime_om
attendance_om = input("Enter OM attendance % : ")
performance_om = input("Enter performance level of OM : ")
status_om = input("Enter OM status : ")

print("\n============================================================")
print(company_name.center(60))
print("==============================================================")

print("\nCompany ID            : ",company_id)
print("Branch                  : ",branch)
print("Address                 : ",address)
print("Telephone               : ",telephone)
print("E-Mail                  : ",email)
print("Website                 : ",website)

print("\n=============================================================")
print(                       employee_profile_report                   )
print("===============================================================")

print("\nEmployee Name         : ",employee_name_ceo)
print("Employee ID             : ",employee_id_ceo)
print("Designation             : ",designation_ceo)

print("\n---------------------------------------------------------------")

print("\nBasic Salary          : ",basic_salary_ceo)
print("Bonus                   : ",bonus_ceo)
print("Overtime Pay            : ",overtime_ceo)
print("Gross Salary            : ",gross_salary_ceo)

print("\n---------------------------------------------------------------")

print("\nAttendance  %         : ",attendance_ceo)
print("Performance             : ",performance_ceo)
print("Status                  : ",Status_ceo)

print("\n================================================================")

print("\n===============================================================")
print(                       employee_profile_report                   )
print("=================================================================")

print("\nEmployee Name         : ",employee_name_md)
print("Employee ID             : ",employee_id_md)
print("Designation             : ",designation_md)

print("\n---------------------------------------------------------------")

print("\nBasic Salary          : ",basic_salary_md)
print("Bonus                   : ",bonus_md)
print("Overttime Pay           : ",overtime_md)
print("Gross Salary            : ",gross_salary_md)

print("\n---------------------------------------------------------------")

print("\nAttendance  %         : ",attendance_md)
print("Performance             : ",performance_md)
print("Status                  : ",status_md)

print("\n================================================================")

print("\n===============================================================")
print(                       employee_profile_report)
print("=================================================================")

print("\nEmployee Name         : ",employee_name_om)
print("Employee Id             : ",employee_id_om)
print("Designation             : ",designation_om)

print("\n----------------------------------------------------------------")

print("\nBasic Salary          : ",basic_salary_om)
print("Bonus                   : ",bonus_om)
print("Overtime Pay            ; ",overtime_om)
print("Gross Salary            : ",gross_salary_om)

print("\n----------------------------------------------------------------")

print("\nAttendance  %         : ",attendance_om)
print("Performance             : ",performance_om)
print("Status                  : ",status_om)

print("\n================================================================")