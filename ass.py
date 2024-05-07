def discount(price, discount):
    if discount > 20:
        print((price - ((price * discount) / 100)))
    else:
        print(price)
discount(30, 15)
discount(45, 40)
def discount1():
    price1 = eval(input("Enter the original price: "))
    discount1 = eval(input("Enter the discount percentage: "))
    if discount1 > 20:
        print((price1 - ((price1 * discount1) / 100)))
    else:
        print(price1)
discount1(3)