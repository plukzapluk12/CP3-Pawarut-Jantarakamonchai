username = input("Username : ")
password = input("Password : ")
if username == "pluk" and password == "123":
    print("---Welcome---")
    print("1.Banana 200")
    print("2.Apple 100")
    userselected = input(">> ")
    if userselected == "1":
        Unit = int(input("How many ? : "))
        print("Total = ",(200*Unit))
    elif userselected == "2":
        Unit = int(input("How many ? : "))
        print("Total = ",(100*Unit))