def shipPrice(a):
    totalPrice = 10.95 + (2.95 * (a - 1))
    print("The total price of the shipping cost is: " + "$" + str(round(totalPrice, 2)))

itemNum = int(input("Enter number of items here: "))
shipPrice(itemNum)