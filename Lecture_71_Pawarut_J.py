menulist = []
pricelist = []
def showbill():
    total = 0
    print("--- Menu ---")
    for i in range(len(menulist)):
        print(menulist[i],int(pricelist[i]))
        total += pricelist[i]
    print(total)
while True:
    menuname = input("Please Enter Menu :")
    if(menuname.lower() == "exit"):
        break
    else :
        price = int(input("Price :"))
        menulist.append(menuname)
        pricelist.append(price)
showbill()


