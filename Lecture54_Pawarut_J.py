def login():
    userName = input("Username : ")
    passWord = input("Password : ")
    if userName == "123" and passWord == "123":
        return showmenu()
    else:
        print("Noob")
        return login()

def showmenu():
    print("----Shop----")
    print("1.Vat Calculator")
    print("2.Price calculator")
    return userselected()

def userselected():
    userselected = int(input(">>"))
    if userselected == 1:
        return vatCalculate((int(input("totalprice:"))))
    elif userselected == 2:
        return priceCalculate()
    else:
        return showmenu()

def vatCalculate(totalprice):
    vat = 7 / 100
    result = totalprice + (totalprice * vat)
    return print(result)

def priceCalculate():
    price1 = int(input("price1 : "))
    price2 = int(input("price2 : "))
    return vatCalculate(price1 + price2)

login()


