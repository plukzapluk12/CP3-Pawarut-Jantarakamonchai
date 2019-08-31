Price = float(input("Price : "))
def Vatcaculate(Price):
    result = Price + Price * (7/100)
    return result
print(Vatcaculate(Price))