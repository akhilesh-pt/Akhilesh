company_name = input("Enter company name : ")
it_support_ticket_report = " IT SUPPORT TICKET REPORT "
ticket_id = input("Enter ticket ID : ")
created_date = input("Enter created date : ")
created_time = input("Enter created time : ")
priority = input("Enter priority : ")
status = input("Enter status : ")
employee_information = " EMPLOYEE INFORMATION "
employee_id = input("Enter employee ID : ")
employee_name = input("Enter employee name : ")
department = input("Enter department : ")
position = input("Enter position : ")
email = input("Enter email : ")
office_location = input("Enter office location : ")
issue_information = " ISSUE INFORMATION "
issue_category = input("Enter issue category : ")
issue_title = input("Enter issue title : ")
issue_description = input("Enter issue description : ")
device_information = " DEVICE INFORMATION "
device_type = input("Enter device type : ")
brand = input("Enter brand : ")
model = input("Enter model : ")
operating_system = input("Enter operating system : ")
ip_adress = input("Enter IP adress : ")
technician_information = "TECHNICIAN INFORMATION"
technician_id = input("Enter technician ID : ")
technician_name = input("Enter technician name : ")
support_team = input("Enter support team : ")
resolution_information = " RESOLUTION INFORMATION "
problem_identified = input("Enter problem identified : ")
action_taken = input("Enter action taken : ")
resolution_status = input("Enter resolution status : ")
resolution_time = input("Enter resolution time : ")
ticket_successfully_processed = " TICKET SUCCESSFULLY PROCESSED "

print("\n=================================================================")
print(company_name.center(60))
print("===================================================================")
print(it_support_ticket_report.center(60))

print("\nTicket ID             : ",ticket_id)
print("Created Date            : ",created_date)
print("Created Time            : ",created_time)
print("Priority                : ",priority)
print("Status                  : ",status)

print("\n-----------------------------------------------------------------")
print(employee_information)
print("-------------------------------------------------------------------")

print("\nEmployee ID           : ",employee_id)
print("Employee Name           : ",employee_name)
print("Department              : ",department)
print("Position                : ",position)
print("Email                   : ",email)
print("Office Location         : ",office_location)

print("\n-----------------------------------------------------------------")
print(issue_information)
print("\n-----------------------------------------------------------------")

print("\nIssue category        : ",issue_category)
print("Issue Title             : ",issue_title)
print("Issue Description       : ",issue_description)

print("\n-----------------------------------------------------------------")
print(device_information)
print("-------------------------------------------------------------------")

print("\nDevice Type           : ",device_type)
print("Brand                   : ",brand)
print("Model                   : ",model)
print("Operating System        : ",operating_system)
print("IP Adress               : ",ip_adress)

print("\n-----------------------------------------------------------------")
print(technician_information)
print("-------------------------------------------------------------------")

print("\nTechnician ID         : ",technician_id)
print("Technician Name         : ",technician_name)
print("Support Team            : ",support_team)

print("\n-----------------------------------------------------------------")
print(resolution_information)
print("-------------------------------------------------------------------")

print("\nProblem Identified    : ",problem_identified)
print("Action Taken            : ",action_taken)
print("Resolution Status       : ",resolution_status)
print("Resolution Time         : ",resolution_time)

print("\n=================================================================")
print(ticket_successfully_processed.center(60))
print("===================================================================")
