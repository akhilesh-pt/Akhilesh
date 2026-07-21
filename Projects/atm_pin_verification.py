attempt = 1

while attempt <= 3:
    pin_number = int(input("Enter PIN : "))

    if pin_number == 1234:
        print("Access Granted")
        break

    else:
        print("Incorrect PIN")
        attempt += 1

if attempt > 3:
    print("Account Blocked")

    