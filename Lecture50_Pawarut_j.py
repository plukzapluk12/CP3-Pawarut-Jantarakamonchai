x = int(input("Fisrt Number : "))
mark = str(input("Mark : "))
y = int(input("Second Number : "))
def addnumber(x,y):
    if mark == "+":
        print(x+y)
    elif mark == "-":
        print(x-y)
    elif mark == "*":
        print(x*y)
    elif mark == "/":
        print(int(x/y))
addnumber(x,y)