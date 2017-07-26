#Shop Manager
import time, sys, os.path, fileinput
from random import randint

class GameInit():
    #handles inital startup
    @staticmethod
    def check_dlc():
        global yes_list, no_list
        #check for DLC/map packs
        ask_dlc = input("Game: Would you like to play with DLC loaded? ")
        if ask_dlc.lower() in ["yes", "y"]:
            file_present = os.path.isfile("dlc/DLC_PIE.dlc")
            file_present2 = os.path.isfile("dlc/DLC_FISH.dlc")
            #loads DLC 1 if file is present
            if file_present == True:
                ask_dlc1 = input("Game: Would you like to load the Packa Pie DLC? ")
                if ask_dlc1.lower() in yes_list:
                    with fileinput.FileInput("dlc/DLC_PIE.dlc", inplace=True, backup='.bak') as file:
                        DLC1 = file.readline()
                        print("Game: Packa Pie DLC loaded.")
                        time.sleep(1)
                else:
                    print("Game: Packa Pie DLC not loaded.")
                    time.sleep(1)
                    
            #loads DLC 2 if file is present
            if file_present2 == True:
                ask_dlc2 = input("Game: Would you like to load the More Fish DLC? ")
                if ask_dlc2.lower() in yes_list:
                    with fileinput.FileInput("dlc/DLC_FISH.dlc", inplace=True, backup='.bak') as file:
                        DLC2 = file.readline()
                        print("Game: More Fish DLC loaded.")
                        time.sleep(1)
                else:
                    print("Game: More Fish DLC not loaded.")
                    time.sleep(1)
                
            elif file_present == False and file_present2 == False:
                print("Game: No DLC installed!")
                      
        if ask_dlc.lower() in ["no", "n"]:
            return
        else:
            return

    @staticmethod
    def variables():
        #sets the variables to default values and creates them on startup or reset
        
        #general
        global username, day, rand_day, cash, level, exp, req_exp, shop, game_version, currency, supported_versions, rent, wages, day_name

        username = "John"
        shop = "Fish n' Chips"
        day = 1
        rand_day = 0
        cash = 25
        level = 1
        exp = 0
        req_exp = 10
        game_version = "v1.3-beta"
        supported_versions = ["v1.2-beta", "v1.3-beta"]
        currency = "£"
        rent = 10
        wages = 10
        day_name = 0
        
        #stock
        global fish, potato, sausage, fishcake, cooked_fish, cooked_potato, cooked_sausage, cooked_fishcake, fish_sellable, potato_sellable, sausage_sellable, fishcake_sellable
        
        fish = 20
        cooked_fish = 0
        fish_sellable = True
        
        potato = 0
        cooked_potato = 0
        potato_sellable = False
        
        sausage = 0
        cooked_sausage = 0
        sausage_sellable = False

        fishcake = 0
        cooked_fishcake = 0
        fishcake_sellable = False

        #prices
        global fish_cost, cooked_fish_cost, potato_cost, cooked_potato_cost, sausage_cost, cooked_sausage_cost, fishcake_cost, cooked_fishcake_cost
        
        fish_cost = 1
        cooked_fish_cost = 1.5
        
        potato_cost = 2
        cooked_potato_cost = 2.5
        
        sausage_cost = 3
        cooked_sausage_cost = 3.5

        fishcake_cost = 3
        cooked_fishcake_cost = 3.5 

        #exp values
        global fish_exp, potato_exp, sausage_exp, fishcake_exp

        fish_exp = 1
        potato_exp = 2
        sausage_exp = 3
        fishcake_exp = 3

        #fail/rand states
        global rand1, rand2, fail1, fail2

        rand1 = False
        rand2 = False
        fail1 = False
        fail2 = False

        #DLC1
        if DLC1 == True:
            global pukkapie, cooked_pukkapie, pukkapie_sellable, pukkapie_cost, cooked_pukkapie_cost, pukkapie_exp
            #pukka pie
            pukkapie = 0
            cooked_pukkapie = 0
            pukkapie_sellable = False
            pukkapie_cost = 1.5
            cooked_pukkapie_cost = 2.5
            pukkapie_exp = 2

        #DLC2
        if DLC2 == True:
            global plaice, cooked_plaice, plaice_sellable, plaice_cost, cooked_plaice_cost, plaice_exp
            #plaice
            plaice = 0
            cooked_plaice = 0
            plaice_sellable = False
            plaice_cost = 2.5
            cooked_plaice_cost = 3.5
            plaice_exp = 3

            global haddock, cooked_haddock, haddock_sellable, haddock_cost, cooked_haddock_cost, haddock_exp
            #haddock
            haddock = 0
            cooked_haddock = 0
            haddock_sellable = False
            haddock_cost = 3
            cooked_haddock_cost = 4.5
            haddock_exp = 4
            

    @staticmethod
    def manager_name():
        #handles the username
        global username, yes_list, no_list
        username = input("Uncle Bob: Hello, I've forgotton your name. What was it again? ")
        #sets default if the input is blank
        if username == "":
            username = "John"
        username_ch = input("Uncle Bob: So you're "+username+" right? ")
        time.sleep(1)
        #asks the user if the if they are sure about their username
        if username_ch.lower() in yes_list:
            print("Uncle Bob: Ah, yes! My brother's kid who's taking the shop from me. I forgot who you were for a minute!")
            return
        if username_ch.lower() in no_list:
            GameInit.manager_name()
            return
        else:
            print("Uncle Bob: What's that? I didn't quite catch that.")
            GameInit.manager_name()

    @staticmethod
    def shop_name():
        #handles the shop
        global shop, yes_list, no_list, username
        time.sleep(1)
        print("Uncle Bob: You might as well re-name the shop as 'Fish n' Chips' might not be as good as what you come up with.")
        time.sleep(1)
        shop = input("Uncle Bob: So "+username+", what would you like the shop to be called? ")
        #sets default if the input is blank
        if shop == "":
            shop = "Fish n' Chips"
        shop_ch = input("Uncle Bob: You want it called "+shop+"? ")
        #asks the user if the if they are sure about the shop name
        if shop_ch.lower() in yes_list:
            if shop.lower() == "fish n' chips":
                print("Uncle Bob: So it was a good name...")
            return
        if shop_ch.lower() in no_list:
            GameInit.shop_name()
            return
        else:
            print("Uncle Bob: What's that "+username+"? I didn't quite catch that.")
            GameInit.shop_name()

    @staticmethod
    def currency_name():
        #handles the shop
        global currency,yes_list, no_list
        currency = input("Uncle Bob: What is the currency you use again? ")
        #sets default if the input is blank
        if currency == "":
            currency = "£"
        currency_ch = input("Uncle Bob: Ah so it's "+currency+"? ")
        #makes sure the user has a value less than or equal to 4
        if len(currency) > 4:
            print("Uncle Bob: That seems to be a bit too long from memory?")
            GameInit.currency_name()
            return
        if currency_ch.lower() in yes_list:
            return
        if currency_ch.lower() in no_list:
            GameInit.currency_name()
            return
        else:
            print("Uncle Bob: What was that kiddo? Say that again for me.")
            GameInit.currency_name()
            return

    @staticmethod  
    def startup():
        #sets up global varaibles used before GameInit.varibles()
        global DLC1, DLC2, yes_list, no_list
        DLC1 = False
        DLC2 = False
        yes_list = ["yes", "y", "yes.", "y.", "yeah", "yh", "yeah.", "yh.", "hells yeah boi", "yeaah","yep", "yep."]
        no_list = ["no", "n", "no.", "n.", "nah", "noo", "nah.", "noo.", "hells nah boi", "naah", "nope", "nope."]
        x_loop = 1
        #runs all the startup stuff
        pre_init = input("Game: Hello, would you like to start a new game? ")
        pre_init = pre_init.lower()

        #runs the variable delcrations
        if pre_init in yes_list:
            GameInit.check_dlc()
            GameInit.variables()
            #launches user-friendly text details
            launching = "Game: Launching"
            for x in range(3):
                launching = launching + "."
                print(launching)
                time.sleep(0.5)
            print("")
            
            GameInit.manager_name()
            GameInit.shop_name()
            GameInit.currency_name()
            GameMain.main()
            return
        
        #asking about loading the game if pre_init input equals no
        if pre_init in no_list:
            ask_load = input("Game: Would you like to load a previous game? ")
            if ask_load in yes_list:
                DataManage.load()
                return
            if ask_load in no_list:
                DataManage.game_quit()
                return
            else:
                print("Game: Please enter a valid reply.")
                GameInit.startup()
        #skips the startup questions if the user is a tester
        if pre_init.lower() in ["default", "bug"]:
            GameInit.variables()
            GameMain.main()
        else:
            print("Game: Please enter a valid reply.")
            GameInit.startup()

    @staticmethod
    def day_costs():
        global cash, rent, wages, currency
        #manages the rent and taxes for the day
        rent_and_wages = rent + wages
        print("Fred: You should pay the rent and the wages for today.")
        print("Fred: That comes to "+currency+str(rent_and_wages)+" "+username+"!")
        time.sleep(1.5)
        if rent_and_wages > cash:
            print("Fred: You don't have enough money boss! I'm sorry but we're going to have to close down!")
            GameInit.game_over()
        else:
            cash = cash - rent_and_wages
            print("Fred: You now have "+currency+str(cash)+" left.")
            
    @staticmethod
    def end():
        #manages all of the end of day prints
        global level, cash, exp, req_exp, currency, day, yes_list, no_list
        print("Fred: Congratulations Boss, you finished the day with "+currency+str(cash)+" overall!")
        print("Fred: You are level "+str(level)+" and have "+str(exp)+"/"+str(req_exp)+" EXP for the next level.")
        #rusn the rent and wages func.
        GameInit.day_costs()
        #changes the day and resets the daytime var.
        daytime = 0
        day = day + 1
        #ask the user to save the game and runs the save function if yes
        ask_sav = input("Game: Would you like to save your game? ")
        ask_sav = ask_sav.lower()
        if ask_sav in yes_list:
            DataManage.save()
        elif ask_sav in no_list:
            print("")
        else:
            print("Game: Please enter a valid response!")

        #ask the user about quitting the game and runs the quit function is yes    
        ask_qui = input("Game: Would you like to quit your game? ")
        ask_qui = ask_qui.lower()
        if ask_qui in yes_list:
            DataManage.game_quit()
            return
        elif ask_qui in no_list:
            return
        else:
            print("Game: Please enter a valid response!")

    @staticmethod
    def buy_stock():
        global yes_list, no_list, DLC1, DLC2, fish, fish_cost, potato, potato_cost, sausage, sausage_cost, fishcake, fishcake_cost, cash, level, currency
        if DLC1 == True:
            global pukkapie, pukkapie_cost
        if DLC2 == True:
            global plaice, plaice_cost, haddock, haddock_cost
        #asks the user if they want to buy stock to sell later on
        ask_stock = input("Fred: Hey boss, would you like to buy some stock this morning (You have "+currency+ str(cash)+")? ")
        if ask_stock.lower() in yes_list:
            #shows how much stock they have and asks them what they want to buy
            print("Fred: Cod Stock: "+str(fish)+", Potato Stock: "+str(potato)+", Sasuage Stock: "+str(sausage)+" and Fishcake Stock: "+str(fishcake)+" ")
            dlc_str = ""
            if DLC1 == True:
                dlc_str = dlc_str + "Pie Stock "+str(pukkapie)+", "
            if DLC2 == True:
                dlc_str = dlc_str + "Plaice Stock: "+str(plaice)+" and Haddock Stock: "+str(haddock)+" "
            print(dlc_str)
            ask_buy = input("Fred: What do you want to buy? ")

            #asks them how many fish they want to buy
            if ask_buy.lower() in ["cod", "cods", "c"]:
                ask_amount = int(input("Fred: How much Cod would you like to order? ("+currency + str(fish_cost) + " a cod) "))
                #checks if the cash is there to buy the stock
                if ask_amount > cash:
                    print("Fred: Sorry, we don't have the money to order that much!")
                    GameInit.buy_stock()
                    return
                else:
                    #adds the stock to the global var. and subtarcts the cost
                    cash = cash - (ask_amount * fish_cost)                
                    fish = fish + ask_amount
                    time.sleep(1.5)
                    return
                
            #asks them how many potatoes they want to buy
            if ask_buy.lower() in ["potato", "potatoes", "p"]:
                #checks if the user is a high enough level to buy the stock to sell
                if level < 3:
                    print("Fred: Sorry! You need to be level 3 to unlock this!")
                    GameInit.buy_stock()
                elif level >= 3:
                    ask_amount = int(input("Fred: How many potatoes would you like to order? ("+currency + str(potato_cost) + " a potato) "))
                    #checks if the cash is there to buy the stock
                    if ask_amount > cash:
                        print("Fred: Sorry, we don't have the money to order that many!")
                        buy_stock()
                        return
                    else:
                        #adds the stock to the global var. and subtarcts the cost
                        cash = cash - (ask_amount * potato_cost)                
                        potato = potato + ask_amount
                        time.sleep(1.5)
                        return
            else:
                print("Game: Please enter a valid reply.")
                GameInit.buy_stock()
                return
                
            #asks them how many sausage they want to buy
            if ask_buy.lower() in ["sausage", "sausages", "s"]:
                #checks if the user is a high enough level to buy the stock to sell
                if level < 5:
                    print("Fred: Sorry! You need to be level 5 to unlock this!")
                    GameInit.buy_stock()
                elif level >= 5:
                    ask_amount = int(input("Fred: How many sausages would you like to order? (" + currency + str(sausage_cost) + " a sausage) "))
                    #checks if the cash is there to buy the stock
                    if ask_amount > cash:
                        print("Fred: Sorry, we don't have the money to order that much!")
                        GameInit.buy_stock()
                        return
                    else:
                        #adds the stock to the global var. and subtarcts the cost
                        cash = cash - (ask_amount * sausage_cost)                
                        sausage = sausage + ask_amount
                        time.sleep(1.5)
                        return
            else:
                print("Game: Please enter a valid reply.")
                GameInit.buy_stock()
                return
            
            #asks them how many fishcake they want to buy
            if ask_buy.lower() in ["fishcake", "fishcakes", "fc"]:
                #checks if the user is a high enough level to buy the stock to sell
                if level < 7:
                    print("Fred: Sorry! You need to be level 7 to unlock this!")
                    GameInit.buy_stock()
                elif level >= 7:
                    ask_amount = int(input("Fred: How many fishcakes would you like to order? (" + currency + str(fishcake_cost) + " a fishcake) "))
                    #checks if the cash is there to buy the stock
                    if ask_amount > cash:
                        print("Fred: Sorry, we don't have the money to order that many!")
                        GameInit.buy_stock()
                        return
                    else:
                        #adds the stock to the global var. and subtarcts the cost
                        cash = cash - (ask_amount * fishcake_cost)                
                        fishcake = fishcake + ask_amount
                        time.sleep(1.5)
                        return
                    
            if ask_buy.lower() in ["pukkapie", "pukka pie", "pie", "pies", "dlc1"]:
                if DLC1 == True:
                    if level < 4:
                        print("Fred: Sorry! You need to be level 4 to unlock this!")
                        GameInit.buy_stock()
                    elif level >= 4:
                        ask_amount = int(input("Fred: How many pies would you like to order? (" + currency + str(pukkapie_cost) + " a pie) "))
                        #checks if the cash is there to buy the stock
                        if ask_amount > cash:
                            print("Fred: Sorry, we don't have the money to order that many!")
                            GameInit.buy_stock()
                            return
                        else:
                            #adds the stock to the global var. and subtarcts the cost
                            cash = cash - (ask_amount * pukkapie_cost)                
                            pukkapie = pukkapie + ask_amount
                            time.sleep(1.5)
                            return
                        
            if ask_buy.lower() in ["plaice", "plaices", "p", "fish2"]:
                if DLC1 == True:
                    if level < 6:
                        print("Fred: Sorry! You need to be level 6 to unlock this!")
                        GameInit.buy_stock()
                    elif level >= 6:
                        ask_amount = int(input("Fred: How much plaice would you like to order? (" + currency + str(plaice_cost) + " a plaice) "))
                        #checks if the cash is there to buy the stock
                        if ask_amount > cash:
                            print("Fred: Sorry, we don't have the money to order that many!")
                            GameInit.buy_stock()
                            return
                        else:
                            #adds the stock to the global var. and subtarcts the cost
                            cash = cash - (ask_amount * plaice_cost)                
                            plaice = plaice + ask_amount
                            time.sleep(1.5)
                            return
                else:
                    print("Game: Error, DLC not found.")

            if ask_buy.lower() in ["haddock", "haddocks", "h", "fish3"]:
                if DLC1 == True:
                    if level < 8:
                        print("Fred: Sorry! You need to be level 8 to unlock this!")
                        GameInit.buy_stock()
                    elif level >= 8:
                        ask_amount = int(input("Fred: How much haddock would you like to order? (" + currency + str(haddock_cost) + " a haddock) "))
                        #checks if the cash is there to buy the stock
                        if ask_amount > cash:
                            print("Fred: Sorry, we don't have the money to order that many!")
                            GameInit.buy_stock()
                            return
                        else:
                            #adds the stock to the global var. and subtarcts the cost
                            cash = cash - (ask_amount * haddock_cost)                
                            haddock = haddock + ask_amount
                            time.sleep(1.5)
                            return
                else:
                    print("Game: Error, DLC not found.")

            ask_reorder = input("Fred: Would you like to place another order? ")
            if ask_reorder in yes_list:
                GameInit.buy_stock()
            if ask_reorder in no_list:
                print("Fred: The order has arrived thanks to Congo Prime and the almost instant delivery!")
                

            else:
                print("Game: Please enter a valid reply.")
                GameInit.buy_stock()
                return
            
        if ask_stock.lower() in no_list:
            print("Fred: We can always order more tomorrow if we need.")
            return

        else:
            return
            
    @staticmethod
    def cook_fish():
        #variables
        global username, fish, cooked_fish, level, cooked_fish_cost, currency, yes_list, no_list

        #asks the user how mucbh fo the stock they want to cook
        print("Fred: Perfect! How many cod would you like to cook this morning? ")
        ask_fish = int(input("Fred: Lastly "+username+", you only have "+str(fish)+": "))
        #checking they have the stock to cook
        if ask_fish > fish:
            print("Fred: Boss, you can't cook more than you have!")
            GameInit.cook_fish()
        else:
            print("Fred: I'll cook the cod now Boss!")    
            time.sleep(1.5)
            #subtracts the fish and adds them to the cooked stock
            fish = fish - ask_fish
            cooked_fish = ask_fish
            print("Fred: Al'ight Boss, "+str(cooked_fish)+" cod were cooked!")
        
        ask_chg = input("Fred: Would you like to change the price today? ")
        if ask_chg in ["yes", "y"]:
            cooked_fish_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_fish_cost)+") "))
            return
        if ask_chg in ["no", "n"]:
            return

    @staticmethod
    def cook_potato():
        #variables
        global potato, cooked_potato, level, potato_sellable, username, cooked_potato_cost, currency, yes_list, no_list
        
        #asks the user how mucbh fo the stock they want to cook
        ask_pots = input("Fred: Would you like to cook chips today? ")
        if ask_pots.lower() in yes_list:
            print("Fred: Sounds great! How many potatoes do you want to cook this morning? ")
            ask_potato = int(input("Fred: By the way, you currently have "+str(potato)+": "))
            #checking they have the stock to cook
            if ask_potato > potato:
                print("Fred: Boss, you can't cook more than you have!")
                GameInit.cook_potato()    
            else:
                print("Fred: I'll cook the potatoes now Boss!")
                time.sleep(1.5)
                #subtracts the fish and adds them to the cooked stock
                potato = potato - ask_potato
                cooked_potato = ask_potato
                print("Fred: Al'ight Boss, "+str(cooked_potato)+" portions of chips were cooked!")
            
        if ask_pots.lower() in no_list:
            potato_sellable = False
            print("Fred: That sounds like a plan boss!")

        ask_chg = input("Fred: Would you like to change the price today? ")
        #changes the price to what the user selects and stores it as a float
        if ask_chg in yes_list:
            cooked_potato_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_potato_cost)+") "))
            return
        if ask_chg in no_list:
            return

    @staticmethod
    def cook_sausage():
        #variables
        global sausage, cooked_sausage, level, sausage_sellable, username, cooked_sausage_cost, currency, yes_list, no_list

        #asks the user how mucbh fo the stock they want to cook
        ask_pots = input("Fred: Would you like to cook sauages today? ")
        if ask_pots.lower() in yes_list:
            print("Fred: Sounds great! How many sausages do you want to cook this morning? ")
            ask_sausage = int(input("Fred: You have "+str(sausages)+": "))
            #checking they have the stock to cook
            if ask_sausage > sausage:
                print("Fred: Boss, you can't cook more than you have!")
                GameInit.cook_sausage()    
            else:
                print("Fred: I'll cook the sausages now Boss!")
                time.sleep(1.5)
                #subtracts the fish and adds them to the cooked stock
                sausage = sausage - ask_sausages
                cooked_sausage = ask_sausages
                print("Fred: Al'ight Boss, "+str(cooked_sausage)+" sausages were cooked!")
            
        if ask_pots.lower() in no_list:
            sausage_sellable = False
            print("Fred: Sounds like a plan "+username+"!")

        ask_chg = input("Fred: Would you like to change the price today? ")
        #changes the price to what the user selects and stores it as a float
        if ask_chg in yes_list:
            cooked_sausage_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_sausage_cost)+") "))
            return
        if ask_chg in no_list:
            return
        
    @staticmethod
    def cook_fishcake():
        #variables
        global fishcake, cooked_fishcake, level, fishcake_sellable, username, cooked_fishcake_cost, currency, yes_list, no_list

        #asks the user how mucbh fo the stock they want to cook
        ask_pots = input("Fred: Would you like to cook fishcakes today? ")
        if ask_pots.lower() in yes_list:
            print("Fred: Sounds great! How many fishcakes do you want to cook this morning? ")
            ask_fishcake = int(input("Fred: You have "+str(fishcake)+": "))
            #checking they have the stock to cook
            if ask_fishcake > fishcake:
                print("Fred: Boss, you can't cook more than you have!")
                GameInit.cook_fishcake()    
            else:
                print("Fred: I'll cook the fishcakes now Boss!")
                time.sleep(1.5)
                #subtracts the fish and adds them to the cooked stock
                fishcake = fishcake - ask_fishcake
                cooked_fishcake = ask_fishcake
                print("Fred: Okay Boss, "+str(cooked_fishcake)+" fishcakes were cooked!")
            
        if ask_pots.lower() in no_list:
            sausage_sellable = False
            print("Fred: Sounds like a plan "+username+"!")

        ask_chg = input("Fred: Would you like to change the price today? ")
        #changes the price to what the user selects and stores it as a float
        if ask_chg in yes_list:
            cooked_fishcake_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_fishcake_cost)+") "))
            return
        if ask_chg in no_list:
            return
        
    @staticmethod
    def cook_pukkapie():
        #variables
        global pukkapie, cooked_pukkapie, pukkapie_sellable, cooked_pukkapie_cost, level, username, currency, yes_list, no_list

        #asks the user how mucbh fo the stock they want to cook
        ask_pots = input("Fred: Would you like to cook pies today? ")
        if ask_pots.lower() in yes_list:
            print("Fred: Sounds great! How many pies do you want to cook this morning? ")
            ask_pukkapie = int(input("Fred: You have "+str(pies)+": "))
            #checking they have the stock to cook
            if ask_pukkapie > pukkapie:
                print("Fred: Boss, you can't cook more than you have!")
                GameInit.cook_pukkapie()    
            else:
                print("Fred: I'll cook the pies now Boss!")
                time.sleep(1.5)
                #subtracts the fish and adds them to the cooked stock
                pukkapie = pukkapie - ask_pukkapie
                cooked_pukkapie = ask_pukkapie
                print("Fred: Okay Boss, "+str(cooked_pukkapie)+" pies were cooked!")
            
        if ask_pots.lower() in no_list:
            sausage_sellable = False
            print("Fred: Sounds like a plan "+username+"!")

        ask_chg = input("Fred: Would you like to change the price today? ")
        #changes the price to what the user selects and stores it as a float
        if ask_chg in yes_list:
            cooked_fishcake_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_pukkapie_cost)+") "))
            return
        if ask_chg in no_list:
            return
        
    @staticmethod
    def cook_plaice():
        #variables
        global plaice, cooked_plaice, plaice_sellable, cooked_plaice_cost, level, username, currency, yes_list, no_list

        #asks the user how mucbh fo the stock they want to cook
        ask_pots = input("Fred: Would you like to cook plaice today? ")
        if ask_pots.lower() in yes_list:
            print("Fred: Sounds great! How much plaice do you want to cook this morning? ")
            ask_plaice = int(input("Fred: You have "+str(plaice)+": "))
            #checking they have the stock to cook
            if ask_plaice > plaice:
                print("Fred: Boss, you can't cook more than you have!")
                GameInit.cook_plaice()    
            else:
                print("Fred: I'll cook the plaice now Boss!")
                time.sleep(1.5)
                #subtracts the fish and adds them to the cooked stock
                plaice = plaice - ask_plaice
                cooked_plaice = ask_plaice
                print("Fred: Okay Boss, "+str(cooked_plaice)+" plaice were cooked!")
            
        if ask_pots.lower() in no_list:
            sausage_sellable = False
            print("Fred: Sounds like a plan "+username+"!")

        ask_chg = input("Fred: Would you like to change the price today? ")
        #changes the price to what the user selects and stores it as a float
        if ask_chg in yes_list:
            cooked_plaice_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_plaice_cost)+") "))
            return
        if ask_chg in no_list:
            return
        
    @staticmethod
    def cook_haddock():
        #variables
        global haddock, cooked_haddock, haddock_sellable, cooked_haddock_cost, level, username, currency, yes_list, no_list

        #asks the user how mucbh fo the stock they want to cook
        ask_pots = input("Fred: Would you like to cook haddock today? ")
        if ask_pots.lower() in yes_list:
            print("Fred: Sounds great! How much haddock do you want to cook this morning? ")
            ask_plaice = int(input("Fred: You have "+str(haddock)+": "))
            #checking they have the stock to cook
            if ask_plaice > plaice:
                print("Fred: Boss, you can't cook more than you have!")
                GameInit.cook_plaice()    
            else:
                print("Fred: I'll cook the haddock now Boss!")
                time.sleep(1.5)
                #subtracts the fish and adds them to the cooked stock
                plaice = plaice - ask_plaice
                cooked_plaice = ask_plaice
                print("Fred: Okay Boss, "+str(cooked_haddock)+" haddock were cooked!")
            
        if ask_pots.lower() in no_list:
            sausage_sellable = False
            print("Fred: Sounds like a plan "+username+"!")

        ask_chg = input("Fred: Would you like to change the price today? ")
        #changes the price to what the user selects and stores it as a float
        if ask_chg in yes_list:
            cooked_plaice_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(cooked_haddock_cost)+") "))
            return
        if ask_chg in no_list:
            return
              
    @staticmethod
    def special_days():
        #special days
        global cash, day, shop, currency, rent, wages, day_name
        #runs the special day code for the first day, the beginning
        if day == 1:
            rw = rent + wages
            print("-= Day 1: The Beginning =-")
            print("Uncle Bob: Welcome to ShopManager "+username+"! You must run "+shop+" inherited from me, your Uncle Bob!")
            print("Uncle Bob: Always remember you have to pay "+currency+str(rw)+" a day in wages and rent!")
            time.sleep(1.5)

        #runs the special day code for the 7th day, the end of week 1
        if day == 7:
            bonus = level * 10
            print("-= Day 7: The First Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra "+currency+bonus+" to get you on your way!")
            cash += bonus
            print("Game: You now have "+currency+str(cash)+"!")
            time.sleep(1.5)

        #runs the special day code for the 14th day, the end of week 2
        if day == 14:
            bonus = level * 20
            print("-= Day 14: The Second Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through a second week. Impressive! Here's an extra "+currency+bonus+" to get you on your way!")
            cash += bonus
            print("Game: You now have "+currency+str(cash)+"!")
            time.sleep(1.5)

        #checks if it isn't a speical day and prints the default day header
        elif day not in [1, 7, 14, rand_day]:
            print("-= Day "+str(day)+" =-")
            time.sleep(1.5)
            if day_name == 0:
                print("-= Monday =-")
                day_name += 1
            if day_name == 1:
                print("-= Tuesday =-")
                day_name += 1
            if day_name == 2:
                print("-= Wednesday =-")
                day_name += 1
            if day_name == 3:
                print("-= Thursday =-")
                day_name += 1
            if day_name == 4:
                print("-= Friday =-")
                day_name += 1
            if day_name == 5:
                print("-= Saturday =-")
                day_name += 1
            if day_name == 6:
                print("-= Sunday =-")
                day_name = 0
        else:
            return

    @staticmethod
    def random_days():
        #picks a random day and runs a special feature
        global day, rand_day, rand1, cash

        #creates a random day number and runs the code if it is equal to the day and runs the leak event
        rand_day = randint(2, 6)
        if (rand_day == day) and (rand1 == False):
            lesscash = level * 5
            print("-= Day "+str(rand_day)+": The Leak =-")
            print("Uncle Bob: It rained hard last night and a leak was found in the shop. You were charged "+currency+"10 to fix it!")
            cash -= lesscash
            print("Uncle Bob: You now have "+currency+str(cash)+" left!")
            rand1 == True

        #creates a random day number and runs the code if it is equal to the day and runs the stock spoiling event
        rand_day2 = randint(8, 13)
        if (rand_day2 == day) and (rand2 == False):
            print("-= Day "+str(rand_day)+": The Spoils =-")
            print("Uncle Bob: Somehow the fridge door was left open causing some of the stock to spoil.")
            fish = fish - rand_day
            print("Uncle Bob: You now have "+str(rand_day)+" less cod.")
            rand2 == True

    @staticmethod
    def game_over():
        #manages the game over state
        global username, fail1, fail2, game_version
        #checks for funny usernames
        if username.lower() == "hudson":
            print("Uncle Bob: It's game over man, game over!")
        if username.lower() == "rick harrison":
            print("Uncle Bob: Your Rick Harrison and that's not longer your paw-- fish and chip shop.")
        if username.lower() == "rick astley":
            print("Uncle Bob: Never gunna fry you up, never batter you down.")

        #checks if the variable(s) are below the threshold
        if cash > 0:
            print("Uncle Bob: You ran out of money, and the shop had to close. Try to mange your money better in the future.")
            fail1 == True
            game_version = "[FAILED]"
            return
        
        if fish > 0:
            print("Uncle Bob: You ran out of cod, and the shop had to close. Try to mange your cod better in the future.")
            fail2 == True
            game_version = "[FAILED]"
            return
        
    @staticmethod
    def stock_info():
        global DLC1, DLC2, yes_list, no_list
        #displays details on the current stock options
        ask_view = input("Fred: Would you like to view details on the stock? ")
        if ask_view.lower() in yes_list:
            print("Fred: Here's the stock book for you boss!")
            print("")
            #fish
            global fish_cost, cooked_fish_cost, fish_exp
            print("Book: Cod\n| Cod Cost: "+str(fish_cost)+" | Cooked Cod Cost: "+str(cooked_fish_cost)+" | Cod EXP: "+str(fish_exp)+" |")
            #potatoes
            if level >= 3:
                global potato_cost, cooked_potato_cost, potato_exp
                print("Book: Potatoes\n| Potato Cost: "+str(potato_cost)+" | Cooked Potato Cost: "+str(cooked_potato_cost)+" | Potato EXP: "+str(potato_exp)+" |")
            else:
                print("Book: Potatoes\n| Potato Cost: ??? | Cooked Potato Cost: ??? | Potato EXP: ??? |")
            #sausage
            if level >= 5:
                global sausage_cost, cooked_sausage_cost, sausage_exp
                print("Book: Sausage\n| Sausage Cost: "+str(sausage_cost)+" | Cooked Sausage Cost: "+str(cooked_sausage_cost)+" | Sausage EXP: "+str(sausage_exp)+" |")
            else:
                print("Book: Sausage\n| Sausage Cost: ??? | Cooked Sausage Cost: ??? | Sausage EXP: ??? |")
            #fishcake
            if level >= 7:
                global fishcake_cost, cooked_fishcake_cost, fishcake_exp
                print("Book: Fishcake\n| Fishcake Cost: "+str(fishcake_cost)+" | Cooked Fishcake Cost: "+str(cooked_fishcake_cost)+" | Fishcake EXP: "+str(fishcake_exp)+" |")
            else:
                print("Book: Fishcake\n| Fishcake Cost: ??? | Cooked Fishcake Cost: ??? | Fishcake EXP: ??? |")
            #pukkapie
            if level >= 4 and DLC1 == True:
                global pukkapie_cost, cooked_pukkapie_cost, pukkapie_exp
                print("Book: Pies\n| Pie Cost: "+str(fishcake_cost)+" | Cooked Pie Cost: "+str(cooked_fishcake_cost)+" | Pie EXP: "+str(fishcake_exp)+" |")
            if DLC1 == True:
                print("Book: Pie\n| Pie Cost: ??? | Cooked Pie Cost: ??? | Pie EXP: ??? |")
            #plaice
            if level >= 6 and DLC2 == True:
                global plaice_cost, cooked_plaice_cost, plaice_exp
                print("Book: Plaice\n| Plaice Cost: "+str(plaice_cost)+" | Cooked Plaice Cost: "+str(cooked_plaice_cost)+" | Plaice EXP: "+str(plaice_exp)+" |")
            elif DLC2 == True:
                print("Book: Plaice\n| Plaice Cost: ??? | Cooked Plaice Cost: ??? | Plaice EXP: ??? |")
            #haddock
            if level >= 8 and DLC2 == True:
                global haddock_cost, cooked_haddock_cost, haddock_exp
                print("Book: Haddock\n| Haddock Cost: "+str(haddock_cost)+" | Cooked Haddock Cost: "+str(cooked_haddock_cost)+" | Haddock EXP: "+str(haddock_exp)+" |")
            elif DLC2 == True:
                print("Book: Haddock\n| Haddock Cost: ??? | Cooked Haddock Cost: ??? | Haddock EXP: ??? |")
            print("")

            time.sleep(5)
        if ask_view.lower() in no_list:
            return

    @staticmethod
    def manage_customers():
        global cooked_fish_cost, cooked_potato_cost, cooked_sausage_cost, cooked_fishcake_cost, DLC1, DLC2, level, hour_exp, tprofit
        global fish_customers, potato_customers, sausage_customers, fishcake_customers, fish_hour_exp, potato_hour_exp, sausage_hour_exp, fishcake_hour_exp
        if DLC1 == True:
            global pukkapie_customers, pukkapie_hour_exp, cooked_pukkapie_cost
        if DLC2 == True:
            global plaice_customers, haddock_customers, cooked_haddock_cost, cooked_plaice_cost, plaice_hour_exp, haddock_hour_exp
            
        #calculaing the amount of customers and exp for fish
        fish_rand_no = level * randint(1, 3)
            
        if cooked_fish_cost < 1:
            fish_rand_no = level * randint(1, 6)
        if 1 <= cooked_potato_cost <= 3:
            fish_rand_no = level * randint(1, 4)
        if 4 < cooked_fish_cost < 10:
            fish_rand_no = level * randint(1, 2)
        if cooked_fish_cost > 10:
            fish_rand_no = 0
            print("Uncle Bob: Those are some expensive cod!")
                
        fish_customers = randint(0, fish_rand_no)
        fish_hour_exp = fish_customers * fish_exp

        #calculaing the amount of customers and exp for potatoes
        if level >= 3:
            potato_rand_no = level * randint(1, 3)
                
            if cooked_potato_cost < 2:
                potato_rand_no = level * randint(1, 6)
            if 2 <= cooked_potato_cost <= 5:
                potato_rand_no = level * randint(1, 4)
            if 6 < cooked_fish_cost < 10:
                fish_rand_no = level * randint(1, 2)
            if cooked_fish_cost > 10:
                potato_rand_no = 0
                print("Uncle Bob: Those are some expensive chips!")
                    
            potato_customers = randint(0, potato_rand_no)
            potato_hour_exp = potato_customers * potato_exp

        #calculaing the amount of customers and exp for sausage
        if level >= 5:
            sausage_rand_no = level * randint(1, 3)
                
            if cooked_sausage_cost < 3:
                sausage_rand_no = level * randint(1, 6)
            if 3 <= cooked_sausage_cost <= 7:
                sausage_rand_no = level * randint(1, 4)
            if 8 < cooked_sausage_cost < 11:
                sausage_rand_no = level * randint(1, 2)
            if cooked_sausage_cost > 12:
                sausage_rand_no = 0
                print("Uncle Bob: Those are some expensive sausages!")
                    
            sausage_customers = randint(0, sausage_rand_no)
            sausage_hour_exp = sausage_customers * sausage_exp

        #calculaing the amount of customers and exp for sausages
        if level >= 7:
            fishcake_rand_no = level * randint(1, 3)
                
            if cooked_fishcake_cost < 3:
                fishcake_rand_no = level * randint(1, 6)
            if 3 <= cooked_fishcake_cost <= 7:
                fishcake_rand_no = level * randint(1, 4)
            if 8 < cooked_fishcake_cost < 11:
                fishcake_rand_no = level * randint(1, 2)
            if cooked_fishcake_cost > 12:
                fishcake_rand_no = 0
                print("Uncle Bob: Those are some expensive fishcakes!")
                    
            fishcake_customers = randint(0, fishcake_rand_no)
            fishcake_hour_exp = fishcake_customers * fishcake_exp

        #calculaing the amount of customers and exp for pie dlc
        if level >= 4 and DLC1 == True:
            pukkapie_rand_no = level * randint(1, 3)
                
            if cooked_pukkapie_cost < 3:
                pukkapie_rand_no = level * randint(1, 6)
            if 3 <= cooked_pukkapie_cost <= 7:
                pukkapie_rand_no = level * randint(1, 4)
            if 8 < cooked_pukkapie_cost < 11:
                pukkapie_rand_no = level * randint(1, 2)
            if cooked_pukkapie_cost > 12:
                pukkapie_rand_no = 0
                print("Uncle Bob: Those are some expensive pies!")
                    
            pukkapie_customers = randint(0, pukkapie_rand_no)
            pukkapie_hour_exp = pukkapie_customers * pukkapie_exp

        #calculaing the amount of customers and exp for plaice - dlc
        if level >= 6 and DLC2 == True:
            plaice_rand_no = level * randint(1, 3)
                
            if cooked_plaice_cost < 2:
                plaice_rand_no = level * randint(1, 3)
            if 2 <= cooked_plaice_cost <= 6:
                plaice_rand_no = level * randint(1, 2)
            if 7 < cooked_plaice_cost < 10:
                plaice_rand_no = level * randint(1, 1)
            if cooked_plaice_cost > 11:
                plaice_rand_no = 0
                print("Uncle Bob: Those are some expensive plaice!")
                    
            plaice_customers = randint(0, plaice_rand_no)
            plaice_hour_exp = plaice_customers * plaice_exp

        #calculaing the amount of customers and exp for plaice - dlc
        if level >= 8 and DLC2 == True:
            haddock_rand_no = level * randint(1, 3)
                
            if cooked_haddock_cost < 4:
                haddock_rand_no = level * randint(1, 3)
            if 2 <= cooked_haddock_cost <= 6:
                haddock_rand_no = level * randint(1, 2)
            if 7 < cooked_haddock_cost < 10:
                haddock_rand_no = level * randint(1, 1)
            if cooked_haddock_cost > 11:
                haddock_rand_no = 0
                print("Uncle Bob: Those are some expensive haddock!")
                    
            haddock_customers = randint(0, haddock_rand_no)
            haddock_hour_exp = haddock_customers * haddock_exp    

    @staticmethod
    def check_stock():
        global cooked_fish, cooked_potato, cooked_fishcake, DLC1, DLC2, level, fish_sellable, potato_sellable, sausage_sellable, fishcake_sellable
        global fish_customers, potato_customers, sausage_customers, fishcake_customers, tprofit
        if DLC1 == True:
            global pukkapie_customers, pukkapie_hour_exp, cooked_pukkapie, pukkapie_sellable
        if DLC2 == True:
            global plaice_customers, haddock_customers, cooked_haddock, haddock_sellable, cooked_plaice, plaice_sellable
            
        if fish_customers > cooked_fish:
            print("Fred: Welp, we're out of cod!")
            fish_sellable = False
            if level < 3:
                GameInit.end()
                return
                
        if (level >= 3) and (potato_customers > cooked_potato):
            print("Fred: Welp, we're out of chips!")
            potato_sellable = False
            if level < 5 and (fish_sellable == False):
                GameInit.end()
                return

        if (level >= 5) and (sausage_customers > cooked_sausage):
            print("Fred: Welp, we're out of sausages!")
            sausage_sellable = False
            if level < 7 and (fish_sellable == False) and potato_sellable == False:
                GameInit.end()
                return
                
        if (level >= 7) and (fishcake_customers > cooked_fishcake):
            print("Fred: Welp, we're out of sausages!")
            fishcake_sellable = False
            if (fish_sellable == False) and (potato_sellable == False) and (sausage_sellable == False):
                GameInit.end()
                return
                
        if (level >= 4) and (pukkapie_customers > cooked_pukkapie) and DLC1 == True:
            print("Fred: Welp, we're out of pies!")
            pukkapie_sellable = False

        if (level >= 6) and (plaice_customers > cooked_plaice) and DLC2 == True:
            print("Fred: Welp, we're out of plaice!")
            plaice_sellable = False

        if (level >= 8) and (haddock_customers > cooked_haddock) and DLC2 == True:
            print("Fred: Welp, we're out of haddock!")
            haddock_sellable = False
                
            #ends the game if the stock is compeltetly gone from all alreas
            if (fish_sellable == False) and (potato_sellable == False) and (sausage_sellable == False) and (fishcake_sellable == False):
                GameInit.end()
                
    @staticmethod
    def sell_stock():
        global cooked_fish, cooked_potato, cooked_fishcake, cooked_fish_cost, cooked_potato_cost, cooked_sausage_cost, cooked_fishcake_cost, cooked_haddock, haddock_sellable, cooked_haddock_cost, cooked_haddock_cost
        global DLC1, DLC2,level, cash, exp, req_exp, fish_sellable, potato_sellable, sausage_sellable, fishcake_sellable, cooked_pukkapie, pukkapie_sellable, cooked_pukkapie_cost, cooked_haddock, haddock_sellable
        global fish_customers, potato_customers, sausage_customers, fishcake_customers, hour_exp, tprofit, fish_hour_exp, potato_hour_exp, sausage_hour_exp, fishcake_hour_exp

        if DLC1 == True:
            global pukkapie_customers, pukkapie_hour_exp
        if DLC2 == True:
            global plaice_customers, haddock_customers, plaice_hour_exp, haddock_hour_exp
            
        #printing the sold fish and chips
        if fish_sellable == True:
            cooked_fish = cooked_fish - fish_customers
            fish_profit = fish_customers * cooked_fish_cost
            hour_exp = hour_exp + fish_hour_exp
            tprofit = tprofit + fish_profit
            
            if fish_customers == 0:
                print("Fred: No customers bought any cod.")
            if fish_customers > 0:
                 print("Fred: "+str(fish_customers)+" customers visted and ordered "+str(fish_customers)+" cod and we now have "+str(cooked_fish)+" cod left.")
            
        if level >= 3 and potato_sellable == True:
            cooked_potato = cooked_potato - potato_customers
            potato_profit = potato_customers * cooked_potato_cost
            hour_exp = hour_exp + potato_hour_exp
            tprofit = tprofit + potato_profit
                
            if potato_customers == 0:
                print("Fred: No customers bought any chips.")
            if potato_customers > 0:
                print("Fred: "+str(potato_customers)+" customers bought "+str(potato_customers)+" portions of chips and we now have "+str(cooked_potato)+" portions left!")

        if level >= 5 and sausage_sellable == True:
            cooked_sausage = cooked_sausage - sausage_customers
            sausage_profit = sausage_customers * cooked_sausage_cost
            hour_exp = hour_exp + sausage_hour_exp
            tprofit = tprofit + sausage_profit

            if sausage_customers == 0:
                print("Fred: No customers bought any sausages.")
            if sausage_customers > 0:
                print("Fred: "+str(sausage_customers)+" customers bought "+str(sausage_customers)+" sausages and we now have "+str(cooked_sausage)+" sausages left!")

        if level >= 7 and fishcake_sellable == True:
            cooked_fishcake = cooked_fishcake - fishcake_customers
            fishcake_profit = fishcake_customers * cooked_fishcake_cost
            hour_exp = hour_exp + fishcake_hour_exp
            tprofit = tprofit + fishcake_profit
                
            if fishcake_customers == 0:
                print("Fred: No customers bought any fishcakes.")
            if fishcake_customers > 0:
                print("Fred: "+str(fishcake_customers)+" customers bought "+str(fishcake_customers)+" sausages and we now have "+str(cooked_fishcake)+" fishcakes left!")

        if level >= 4 and pukkapie_sellable == True and DLC1 == True:
            cooked_pukkapie = cooked_pukkapie - pukkapie_customers
            pukkapie_profit = pukkapie_customers * cooked_pukkapie_cost
            hour_exp = hour_exp + pukkapie_hour_exp
            tprofit = tprofit + pukkapie_profit
                
            if pukkapie_customers == 0:
                print("Fred: No customers bought any pies.")
            if pukkapie_customers > 0:
                print("Fred: "+str(pukkapie_customers)+" customers bought "+str(pukkapie_customers)+" pies and we now have "+str(cooked_pukkapie)+" pies left!")

        if level >= 6 and plaice_sellable == True and DLC2 == True:
            cooked_plaice = cooked_plaice - plaice_customers
            plaice_profit = plaice_customers * cooked_plaice_cost
            hour_exp = hour_exp + plaice_hour_exp
            tprofit = tprofit + plaice_profit
                
            if plaice_customers == 0:
                print("Fred: No customers bought any plaice.")
            if plaice_customers > 0:
                print("Fred: "+str(plaice_customers)+" customers bought "+str(plaice_customers)+" plaice and we now have "+str(cooked_plaice)+" plaice left!")

        if level >= 8 and haddock_sellable == True and DLC2 == True:
            cooked_haddock = cooked_haddock - haddock_customers
            haddock_profit = haddock_customers * cooked_haddock_cost
            hour_exp = hour_exp + haddock_hour_exp
            tprofit = tprofit + haddock_profit
                
            if haddock_customers == 0:
                print("Fred: No customers bought any haddock.")
            if haddock_customers > 0:
                print("Fred: "+str(haddock_customers)+" customers bought "+str(haddock_customers)+" haddock and we now have "+str(haddock_plaice)+" haddock left!")

    @staticmethod
    def calc_exp():
        global exp, cash, level, req_exp, currency
        cash = cash + tprofit
        exp = exp + hour_exp
        print("Fred: From this, you've made "+currency+str(tprofit)+" and gained "+str(hour_exp)+" EXP.")

        #checking if the user meets the requirements for a level up
        if exp >= req_exp:
            level = level + 1
            exp = exp - req_exp
            req_exp = req_exp * 2
            print("Uncle Bob: Congratulations! You levelled up to "+str(level)+" and gain more reputation!")

    @staticmethod
    def day_time():
        global daytime
        print("Game: "+str((daytime + 3))+":00pm")
        time.sleep(2)
        
class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while (fail1 == False) or (fail2 == False):
            print("")
            GameMain.generic_day()

    @staticmethod
    def generic_day():
        #global imports
        global cooked_fish, cooked_potato, cooked_fishcake, cooked_fish_cost, cooked_potato_cost, cooked_sausage_cost, cooked_fishcake_cost, cooked_haddock, haddock_sellable, cooked_haddock_cost, cooked_haddock_cost
        global DLC1, DLC2,level, cash, exp, req_exp, fish_sellable, potato_sellable, sausage_sellable, fishcake_sellable, cooked_pukkapie, pukkapie_sellable, cooked_pukkapie_cost, cooked_haddock, haddock_sellable
        global hour_exp, tprofit, daytime
        #start of day
        GameInit.random_days()
        GameInit.special_days()
        GameInit.stock_info()
        GameInit.buy_stock()
        GameInit.cook_fish()
        if level >= 3:
            GameInit.cook_potato()
        if level >= 5:
            GameInit.cook_sausage()
        if level >= 7:
            GameInit.cook_fishcake()
        if level >= 4 and DLC1 == True:
            GameInit.cook_pukkapie()
        if level >= 6 and DLC2 == True:
            GameInit.cook_plaice()            
        if level >= 8 and DLC2 == True:
            GameInit.cook_haddock()
            
        #middle section of day
        choice = randint(0, 3)
        if choice == 0:
            print("Fred: Lets open up for the day "+username+"!")
        if choice == 1:
            print("Fred: Lets get ready to open up to the world "+username+".")
        if choice == 2:
            print("Fred: Time to get ready for work "+username+".")
        if choice == 3:
            print("Fred: Time to get the shop ready to open up "+username+"!")
            
        tprofit = 0
        daytime = 0
        texp = 0
        potato_customers = 0
        sausage_customers = 0
        potato_profit = 0
        sausage_profit = 0
        fishcake_profit = 0

        while True:
            #checking if the the daytime is past 9pm
            if daytime >= 7:
                GameInit.end()
                return

            #reseting variables
            tprofit = 0
            hour_exp = 0
                
            #printing the current time of day
            GameInit.day_time()

            #calculate customers and exp
            GameInit.manage_customers()
                   
            #checking if there is stock left
            GameInit.check_stock()

            #sell the stock
            GameInit.sell_stock()
            
            #calculating the profits, exp and cash for the day
            GameInit.calc_exp()
            
            #checking for the end of the day using var 'daytime'
            if daytime >= 7:
                if (fish_sellable == False) and (potato_sellable == False):
                    return
                GameInit.game_over()
                GameInit.end()
                if fail1 == True:
                    GameInit.save()
                    sys.exit()
                if fail2 == True:
                    sys.exit()
            else:
                daytime = daytime + 1
            
class DataManage():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        global fail1, fail2, game_version, DLC1
        save_name = input("Game: What would you like the save file to be called? ")
        print("Game: Saving Game...")
        with open(save_name+".shs", "w") as file:
            #saves all the variables for the next load
            file.write(game_version)
            file.write("\n")
            file.write(username)
            file.write("\n")
            file.write(shop)
            file.write("\n")
            file.write(str(fish))
            file.write("\n")
            file.write(str(potato))
            file.write("\n")
            file.write(str(sausage))
            file.write("\n")
            file.write(str(cooked_fish_cost))
            file.write("\n")
            file.write(str(cooked_potato_cost))
            file.write("\n")
            file.write(str(cooked_sausage_cost))
            file.write("\n")
            file.write(str(day))
            file.write("\n")
            file.write(str(level))
            file.write("\n")
            file.write(str(cash))
            file.write("\n")
            file.write(str(exp))
            file.write("\n")
            file.write(str(req_exp))
            file.write("\n")
            file.write(str(currency))
            file.write("\n")
            file.write(str(fishcake))
            file.write("\n")
            file.write(str(cooked_fishcake_cost))
            file.write("\n")
            if DLC1 == True:
                file.write(str(pukkapie))
                file.write("\n")
                file.write(str(cooked_pukkapie_cost))
                file.write("\n")
            if DLC2 == True:
                file.write(str(plaice))
                file.write("\n")
                file.write(str(cooked_plaice_cost))
                file1.write("\n")
                file.write(str(haddock))
                file.write("\n")
                file.write(str(cooked_haddock_cost))
                file1.write("\n")
            print("Game: Game Saved!")

    @staticmethod
    def load():
        #handles game loading
        save_name = input("Game: What is the name of the save file? ")
        print("Game: Loading Game...")
        GameInit.variables()

        global username, shop, day, level, cash, supported_versions, fish, potato, sausage, cooked_fish,cost, cooked_potato_cost, cooked_sausage_cost, exp, req_exp, game_version, currency
        global fishcake, cooked_fishcake_cost
        
        with open(save_name+".shs", "r+") as file:
            #checking the users game version
            game_version_load = file.readline().replace("\n","")
            if not game_version_load == game_version:
                print("Game: Error, save file is outdated.\nGame: Save: "+game_version_load+", Current: "+game_version+".")
                if game_version_load in supported_versions:
                    print("Game: However this version's save is still supported.")
                else:
                    print("Game: Rebooting...")
                    print("\n\n\n")
                    GameInit.startup()
                    return
        
            #username
            username = file.readline().replace("\n", "")

            #shop
            shop = file.readline().replace("\n", "")
        
            #fish
            fish = int(file.readline().replace("\n", ""))
        
            #potato
            potato = int(file.readline().replace("\n", ""))

            #sausage
            sausage = int(file.readline().replace("\n", ""))

            #cooked fish cost
            cooked_fish_cost = float(file.readline().replace("\n", ""))
        
            #cooked potato cost
            cooked_potato_cost = float(file.readline().replace("\n", ""))

            #cooked sausage cost
            cooked_sausage_cost = float(file.readline().replace("\n", ""))

            #day
            day = int(file.readline().replace("\n", ""))

            #level
            level = int(file.readline().replace("\n", ""))

            #cash
            cash = float(file.readline().replace("\n", ""))

            #exp
            exp = int(file.readline().replace("\n", ""))

            #req_exp
            req_exp = int(file.readline().replace("\n", ""))
        
            #currency
            currency = file.readline().replace("\n", "")

            #fishcake
            fishcake = int(file.readline().replace("\n", ""))
        
            #cooked fishcake cost
            cooked_fishcake_cost = float(file.readline().replace("\n", ""))

            if DLC1 == True:
                #pukkapie
                pukkapie = int(file.readline().replace("\n", ""))

                #cooked pukkapie cost
                cooked_pukkapie_cost = float(file.readline().replace("\n", ""))

            if DLC2 == True:
                #plaice
                plaice = int(file.readline().replace("\n", ""))

                #cooked plaice cost
                cooked_plaice_cost = float(file.readline().replace("\n", ""))
    
                #haddock
                haddock = int(file.readline().replace("\n", ""))

                #cooked haddock cost
                cooked_haddock_cost = float(file.readline().replace("\n", ""))
                
            print("Game: Game Loaded!")
            GameMain.main()

    @staticmethod
    def game_quit():
        ask_quit = input("Game: Are you sure about this? ")
        if ask_quit in ["yes", "y"]:
            sys.exit()
            return
        if ask_quit in ["no", "n"]:
            ask_quit2 = input("Game: Would you like to restart? ")
            if ask_quit2 in ["yes", "y"]:
                print("\n \n \n")
                GameInit.variables()
                GameInit.startup()
                return
            if ask_quit in ["no", "n"]:
                return
        
GameInit.startup()
