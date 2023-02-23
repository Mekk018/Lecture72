menuList = []

def showBill():
    print("-----FOOD CENTER-----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], "THB")

while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price(THB) :")
        menuList.append([menuName, menuPrice])

showBill() 