#Define the menu of restaurant
menu={
    "Pizza":50,
    "pasta":40,
    "Burger":60,
    "Salad":70,
    "Coffee":80,
    
}
#Greet
print("Welcome to Our Restaurant")
print("Pizza:Rs40\nPasta:Rs50\nBurger:Rs60\nSalad:Rs70\nCoffee:Rs80\n")




item1 = input("Enter the name of item you want to order= ")
def hotelMenu():
    c_orders =0
    if item1 in menu:
        c_orders += menu[item1] #0+50
        print(f'Your item {item1} has been added to your order')
    else:
        print(f'Ordered item {item1} is not available yet!')
    another_order = input('Do you want to add another item?(Yes/No)')
    if another_order == "Yes" :
        item2 = input('Enter the name of second item =')
        if item2 in menu:
            c_orders += menu[item2]
            print(f'Item {item2} has been added to order')
        else:
            print(f'Ordered item {item2} is not available!')
    
    print(f'The total amount of items to pay is {c_orders}')
    
while True:
    hotelMenu()