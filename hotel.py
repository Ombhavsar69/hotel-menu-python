menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,


}
#Greet
print("Welcome to Python restaurant")
print("Pizza:Rs40\n Pasta:Rs50\n Burger: Rs60\nSalad: Rs70\n Coffee: Rs80 ")

order_total= 0
#80 + 70=150

item_1=input("Enter thee name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item{item_1} has been addded to your order")

else:
    print(f"Ordered item {item_1} is not available yet!" )
    another_order =input("do you want t0 add another item?(Yes/No) ")
    if another_order =="Yes":
        item_2 =input("Enter the name of the second item= ")
        if item_2 in menu:
            order_total +=menu[item_2]
        (f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item {item_2} is not avaialble!")

        print(f"The Total amount of items is{order_total} ") 