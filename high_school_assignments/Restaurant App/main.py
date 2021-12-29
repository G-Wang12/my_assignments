"""
Gordon Wang
Restaurant Name: Hardcore Burgers
"""
order_list = []
#this is a function created to save the amount of lines needed in the code
#Instead of using multiple lines to ask for the amount of each order and adding the cost of an order to the subtotal, only one line is needed for each order by using this function
#the function will also print a short message each time the user orders a dish
def subtotal_calculation(price, subtotal, menu, dish):
    #the amount variable will ask for the quantity of each dish the user wants
    amount = int(input("how many?"))
    #after knowing the quantity of the dish the additional cost will be added to the subtotal 
    #the subtotal(I will talk about this variable later) is always getting rounded to two decimal places each time it is modified
    subtotal = round((subtotal + price * amount), 2)
    print("Order taken. Thank you. Returning to " + menu + " menu.")
    order_list.append([dish, amount, price])
    #the subtotal will be returned to the submenu function where it will be the new subtotal
    return subtotal
#this is the function for the appetizers menu
def appetizers(subtotal):
    #a while loop is used in every submenu function so the user can stay in the submenu until they explicitly chooses to go back to the main menu.
    while True:
        #a list of options are printed for the user to choose from
        print("\nAPPETIZERS\n\n1) cheese nachos - $4.99\n2) caeser salad - $3.99\n3) cheese corndog - $3.99\n\nEnter 4 to go back to main menu\n")
        print("Your current subtotal is " + "$" + str(subtotal) + "\n")
        #in each submenu there will be an user_action input variable asking the user for their preferred action
        user_action = input("Which dish would you like to order? Enter the number shown before the dish: ")
        if user_action == "1":
            #the built-in try and except function will be used for every user input that happens in this program
            #this is done to make sure the code doesn't stop due to an input error
            #the code will print invalid value and go back to the submenu that the user was in
            try:
                #the subtotal_calculation function is used in this case so that only one line is needed
                #the price of the dish is placed in the first parameter for the function to calculate with, the current subtotal will also be needed in the second parameter 
                #the last parameter contains the name of the submenu so it can be displayed as part of the short text printed in the subtotal_calculation function
                #the current subtotal needs to be changed to the new subtotal value calculated in the subtotal_calculation function. That's why there's a "subtotal =" part
                subtotal = subtotal_calculation(4.99, subtotal, "Appetizers", "cheese nachos\t\t\t")
                #order_list.append("cheese nachos")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "2":
            try:
                #order_list.append("caeser salad")
                subtotal = subtotal_calculation(3.99, subtotal, "Appetizers", "caeser salad\t\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "3":
            try:
                #order_list.append("cheese corndog")
                subtotal = subtotal_calculation(3.99, subtotal, "Appetizers", "cheese corndog\t\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        #this elif is the only way the user can break out of this submenu. The options printed for the user has instructed the user to enter 4 if they want to go back to the main menu
        elif user_action == "4":
            break
        else:
            print("\nInvalid input. Please try again.")
            continue
    #after the while loop breaks the user will head back to the main menu with the subtotal value returned back
    return subtotal
#this is the function for the main courses menu
#note that pretty much all the features in this function are in the same format as the previous appetizers function except with different values and options
#I will not explain a lot of the features again
def main_courses(subtotal):
    while True:
        print("\nMAIN COURSES\n\n1) classic cheese burger - $8.99\n2) chicken burger - $8.99\n3) beyond meat burger - $9.99\n4) bacon burger - $10.99\n\nEnter 5 to go back to main menu\n")
        print("Your current subtotal is " + "$" + str(subtotal) + "\n")
        user_action = input("Which dish would you like to order? Enter the number shown before the dish: ")
        if user_action == "1":
            try:
                subtotal = subtotal_calculation(8.99, subtotal, "Main Courses", "classic cheese burger\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "2":
            try:
                subtotal = subtotal_calculation(8.99, subtotal, "Main Courses", "chicken burger\t\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "3":
            try:
                subtotal = subtotal_calculation(9.99, subtotal, "Main Courses", "beyond meat burger\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "4":
            try:
                subtotal = subtotal_calculation(10.99, subtotal, "Main Courses", "bacon burger\t\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "5":
            break
        else:
            print("\nInvalid input. Please try again.")
            continue
    return subtotal
#this is the function for the desserts menu
#note that pretty much all the features in this function are in the same format as the previous appetizers function except with different values and options
#I will not explain a lot of the features again
def desserts(subtotal):
    while True:
        print("\nDESSERTS\n\n1) Oreo ice cream - $3.99/cone\n2) homebaked chocolate chip cookies - $1.99/each\n3) chocolate cake - $3.99/slice\n\nEnter 4 to go back to main menu")
        print("Your current subtotal is " + "$" + str(subtotal) + "\n")
        user_action = input("Which dish would you like to order? Enter the number shown before the dish: ")
        if user_action == "1":
            try:
                subtotal = subtotal_calculation(3.99, subtotal, "Desserts", "Oreo ice cream\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "2":
            try:
                subtotal = subtotal_calculation(1.99, subtotal, "Desserts", "homebaked chocolate chip cookies")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "3":
            try:
                subtotal = subtotal_calculation(3.99, subtotal, "Desserts", "chocolate cake\t\t\t")
            except ValueError:
                print("\nInvalid input. Please try again.")
            continue
        elif user_action == "4":
            break
        else:
            print("\nInvalid input. Please try again.")
            continue
    return subtotal
#this is the function for the logo of the restaurant
def resto_logo():
    #the restaurant logo is returned so it can be displayed when called inside a print function
    return "🔥 Hardcore Burgers🔥"
#this is the function that would display the final receipt for the user
def calculate_bill(subtotal):
    #this while loop is designed so that the user would have to enter a valid number for the tip before going to the next step
    while True:
        #like in previous functions, the try and except is there to make sure the function doesn't stop from value errors
        try:
            print("")
            tip = float(input("What tip in dollar would you like to give?"))
            #if the try works and the tip is a positive number, the user will break out of the loop
            if tip >=0:
                break
            print("\nInvalid input. Please try again.")
            continue
        except ValueError:
            print("\nInvalid input. Please try again.")
            #if there's a value error the process will repeat
            continue
    print("ITEM\t\t\t\t\tQTY\tPRICE\tAMOUNT")
    for dish in order_list:
        amount = order_list.count(dish)
        print(dish[0] + "\t" + str(dish[1]) + "\t$" + str(dish[2]) + "\t$" + str(round(dish[2] * dish[1], 2)))
    #the tax variable is the calculated tax
    tax = round((0.13 * (subtotal)), 2)
    #add the subtotal with the tip and tax to get the final total fee
    #this value will be stored in the final_total variable after also getting rounded to 2 decimal places in the same line
    final_total = round((subtotal + tip + tax), 2)
    #print these values by converting any int or float to str. 
    print("\nsubtotal: $" + str(subtotal) + "\n" + "tip: $" + str(tip) + "\n" + "tax: $" + str(tax) + "\n" + "Total: $" + str(final_total) + "\n\n" + "Thank you for dining at Hardcore Burgers. Come again!")
#this is the main menu function. It will call the other functions created in response to the user's input
#the subtotal variable is started in the main_menu function as its parameter
def main_menu(subtotal):
    #the while loop is used to be able to start the main menu again in a case of invalid value
    while True:
        print("\nMAIN MENU\n")
        print("***each action below is labelled with a number. Select the respective number of the action you want.\n\n1) order appetizers\n2) order main courses\n3) order deserts\n4) calculate the bill\n")
        print("Your current subtotal is " + "$" + str(subtotal) + "\n")
        user_action = input("Type the action here: ")
        #once the user inputs a valid action, they will be directed to the function made for that action with the current subtotal transferred through parameters
        #the new subtotal will be returned once the user has ordered and wants to go back to the main menu
        #the subtotal value of the main menu will be equal to the value returned
        if user_action == "1":
            subtotal = appetizers(subtotal)
            #after each function is done the while loop will restart so the user can see the main menu again and choose another option
            continue
        elif user_action == "2":
            subtotal = main_courses(subtotal)
            continue
        elif user_action == "3":
            subtotal = desserts(subtotal)
            continue
        elif user_action == "4":
            calculate_bill(subtotal)
            #the main menu while loop will break here once the calculate_bill function finishes displaying the bill
            #that will let the app finish running
            break
        else:
            print("\nInvalid input. Please try again.")
            continue
#this is the first line of text that the app should display
#the function to get the restaurant logo has a return value that can be printed
print("Welcome to " + resto_logo() + "!")
#the main menu function is called to start the process of ordering food
#notice it has a parameter of zero. That is the initical subtotal value
main_menu(0)
