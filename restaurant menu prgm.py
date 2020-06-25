items = [
    "01-Idli(Rs.20)",
    "02-Puri(Rs.35)",
    "03-Dosa(Rs.40)",
    "04-Vada(Rs.10)",
    "05-Parcel(Rs.5)",
]
prices = [20, 35, 40, 10, 5]


class Owner:
    def __init__(self):
        self.items = items
        self.prices = prices

    def updateItem(self, item, price):
        self.items.append(item)
        self.prices.append(price)


class Customer:
    def __init__(self):
        self.items = items
        self.prices = prices
        self.select = {}
        self.total = 0

    def showMenu(self):
        print("\t\t\t\t\t  -------------------")
        print("\t\t\t\t\t  Joyson's Cafe Treat")
        print("\t\t\t\t\t  -------------------")
        print("\t\t\t\t\t   --:Menu List:--\n")
        print("\t\t\t\t\t   Code Item Price")
        for i in self.items:
            print("\t\t\t\t\t  ", i)
        print("\t\t\t\t\t  -------------------")
        print("\t\t\t\t\t  ", "--Print Bill(X)--")

    def selectItems(self, item, quantity):
        for dish in items:
            if dish[:2] == item:
                if dish in self.select:
                    self.select[dish] = (
                        prices[items.index(dish)],
                        quantity + self.select[dish][1],
                    )
                else:
                    self.select[dish] = (prices[items.index(dish)], quantity)

    def calculateBill(self):
        for i in self.select:
            self.total += self.select[i][0] * self.select[i][1]
        return int(self.total)

    def generateBill(self):
        SGST = CGST = self.calculateBill() * 0.06
        print(
            "\t\t\t[---------------------------------------------------------------------]"
        )
        print(
            "\t\t\t|                          Joyson's Cafe Treat                        |"
        )
        print(
            "\t\t\t|                             --:Your Bill:--                         |"
        )
        print(
            "\t\t\t|---------------------------------------------------------------------|"
        )
        print(
            "\t\t\t|Code-Item                               Nos      Price    Total      |"
        )
        for var in self.select:
            print(
                f"\t\t\t|{var}{' '*(40-len(var))}x{self.select[var][1]}{' '*(8-len(str(self.select[var][1])))}x{self.select[var][0]}{' '*(8-len(str(self.select[var][0])))}Rs.{self.select[var][0]*self.select[var][1]}{' '*(11-len('Rs.'+str(+self.select[var][0]*self.select[var][1])))}|"
            )
        print(
            f"\t\t\t|CGST(6%){' '*(58-len('CGST(6%)'))}Rs.{SGST}{' '*(11-len('Rs.'+str(SGST)))}|"
        )
        print(
            f"\t\t\t|SGST(6%){' '*(58-len('CGST(6%)'))}Rs.{CGST}{' '*(11-len('Rs.'+str(CGST)))}|"
        )
        print(
            f"\t\t\t|Total{' '*(58-len('Total'))}Rs.{int(self.total + CGST + SGST)}{' '*(11-len('Rs.'+str(int(self.total+CGST+SGST))))}|"
        )
        print(
            "\t\t\t[---------------------------------------------------------------------]"
        )


if __name__ == "__main__":
    admin = Owner()
    admin.updateItem("06-Masala Dosa(Rs.50)", 50)
    cust1 = Customer()
    cust1.showMenu()
    while True:
        print()
        choice = input("\t\t\tCode: ")
        if choice == "X":
            print()
            cust1.generateBill()
            break
        elif choice in [str(i[:2]) for i in admin.items]:
            quantity = int(input("\t\t\tNos: "))
            cust1.selectItems(choice, quantity)
        else:
            print("Sorry.. This dish is not available.. Try others..")
            cust1.showMenu()
            continue
