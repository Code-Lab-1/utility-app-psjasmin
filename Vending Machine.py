## CODELAB I | ASSESSMENT 2: Utility App
## Vending Machine program using the Python programming language.

def vendingmachine():

    ##-----DRINKS-----##
    a = {'item_no': 'A1', 'item': 'Evian Water Bottle ', 'price': 8.0, 'stock': 5}
    b = {'item_no': 'B2', 'item': 'Mocha Frappuccino  ', 'price': 9.5, 'stock': 3}
    c = {'item_no': 'C3', 'item': 'Coca-Cola          ', 'price': 2.0, 'stock': 4}
    d = {'item_no': 'D4', 'item': 'Gatorade           ', 'price': 5.5, 'stock': 2}
    e = {'item_no': 'E5', 'item': 'Vimto Juice        ', 'price': 2.0, 'stock': 3}

    ##-----SNACKS-----##
    f = {'item_no': 'F6', 'item': 'Maltesers          ', 'price': 3.0, 'stock': 3}
    g = {'item_no': 'G7', 'item': 'Haribo Goldbears   ', 'price': 1.5, 'stock': 1}
    h = {'item_no': 'H8', 'item': 'Lays Chips         ', 'price': 2.0, 'stock': 5}
    i = {'item_no': 'I9', 'item': 'Marie Biscuits     ', 'price': 2.5, 'stock': 4}
    j = {'item_no': 'J0', 'item': 'Chips Ahoy!        ', 'price': 5.0, 'stock': 2}
    
    menu = [a, b, c, d, e, f, g, h, i, j]
    snacks = [f, g, h, i, j]
    drinks = [a, b, c, d, e]
    
    print('''\n\033[1;33m
     █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
     ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄\033[0m''')

    ## -----Displaying items & prices in the vending machine----- ##
    def show(menu):
        # STOCK SYSTEM (DRINKS)
        for item in drinks:
            if item.get('stock') == 0:
                drinks.remove(item)
    
        print("""\n            ┌───────┬────────────────────┬───────┬───────┐
            │ Item# │        Item        │ Price │ Stock │
            ├───────┴────────────────────┴───────┴───────┤
            │                 \033[1m-DRINKS-\033[0m                   │
            ├───────┬────────────────────┬───────┬───────┤""")

        #Displaying list of drinks available in the menu
        for item in drinks:
            print(f"            │ {item.get('item_no')}    │ {item.get('item')}│   {item.get('price')} │  ({item.get('stock')})  │")
        
        # STOCK SYSTEM (SNACKS)
        for item in snacks:      
            if item.get('stock') == 0:
                snacks.remove(item)
        
        print("""            ├───────┴────────────────────┴───────┴───────┤
            │                 \033[1m-SNACKS-\033[0m                   │
            ├───────┬────────────────────┬───────┬───────┤""")
        
        # Displaying list of snacks available in the menu
        for item in snacks:
            print(f"            │ {item.get('item_no')}    │ {item.get('item')}│   {item.get('price')} │  ({item.get('stock')})  │")
        print("            └───────┴────────────────────┴───────┴───────┘")

    continueToBuy = True

    ## -----Managing Money----- ##
    money = float(input("\n                  Insert an amount of money: "))

    ## -----Showing Selections----- ##
    while continueToBuy == True:
        show(menu)

        # User selecting an item (Shows the user's selections)
        print("\n           +----------------------------------------------+")
        selection = input("                           \033[1m\033[1;35mMAKE A SELECTION\n           \033[1;37mEnter the Item# of the item you want to get:\033[0m ")
        
        for item in menu:
            if selection == item.get('item_no'):
                selection = item               
                price = selection.get('price')
                while money < price: # when money inserted is not enought for the item
                    print("\n            \033[1;31mMoney inserted is not enough.\033[0m")
                    money = money + float(input("            Please enter " + "\033[1m\033[1;31m" + str(price - money) + "\033[0m" + " more: "))
                
                # When a product is dispensed
                print(f"""\n                           \033[1;32m{selection.get('item')} 
                           has been dispensed!\033[0m
           +----------------------------------------------+""")
                
                selection['stock'] -= 1 # Updating Item Stocks
                
                ## -----SUGGESTING PURCHASES----- ##
                if selection.get('item_no') == 'A1':
                    print("\n         \x1B[3m> How about Maltesers to go with your Water Bottle?\x1B[0m") #italicized text
                elif selection.get('item_no') == 'F6':
                    print("\n         \x1B[3m> How about an Evian Water Bottle to go with your Maltesers?\x1B[0m")
                elif selection.get('item_no') == 'B2':
                    print("\n         \x1B[3m> How about Marie Biscuits to go with your Mocha Frappuccino?\x1B[0m")
                elif selection.get('item_no') == 'I9':
                    print("\n         \x1B[3m> How about a Mocha Frappucino to go with your Marie Biscuits?\x1B[0m")
                elif selection.get('item_no') == 'C3':
                    print("\n         \x1B[3m> How about some Chips Ahoy! to go with your Coca-Cola?\x1B[0m")
                elif selection.get('item_no') == 'J0':
                    print("\n         \x1B[3m> How about a Coca-Cola to go with your Chips Ahoy?\x1B[0m")
                elif selection.get('item_no') == 'D4':
                    print("\n         \x1B[3m> How about Lays Chips to go with your Gatorade?\x1B[0m")
                elif selection.get('item_no') == 'H8':
                    print("\n         \x1B[3m> How about a Gatorade to go with your Lays Chips?\x1B[0m")
                elif selection.get('item_no') == 'E5':
                    print("\n         \x1B[3m> How about a Haribo Goldbear to go with your Vimto Juice?\x1B[0m")
                else:
                    print("\n         \x1B[3m> How about Vimto Juice to go with your Haribo Goldbears?\x1B[0m")

                money -= price
                print("\n                          \033[1;35mCash Remaining: $" + str(money) + "\033[0m") #shows available cash

                choose = input("           \033[1;37mDo you want to purchase more items?\033[0m (\033[1;32m1-Yes\033[0m | \033[1;31m2-No):\033[0m  ")
                if choose == '2':
                    continueToBuy = False
                    if money != 0:
                        print(f"\n                          \033[1mYour change is ${str(money)}\033[0m") #tells the user their change
                        money = 0
                        print("""                \033[1;33m┌──────────────────────────────────────┐
                │ Thank You! Enjoy Your Purchase(s) :) │
                └──────────────────────────────────────┘\033[0m\n""")
                        break                        
                    else:
                        print("""            
                \033[1;33m┌──────────────────────────────────────┐
                │ Thank You! Enjoy Your Purchase(s) :) │
                └──────────────────────────────────────┘\033[0m\n""")
                        break  
                else:
                    continue

vendingmachine()