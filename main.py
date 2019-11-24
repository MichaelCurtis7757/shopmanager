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
            
            if file_present == True:
                with fileinput.FileInput("dlc/DLC_PIE.dlc", inplace=True, backup='.bak') as file:
                    global DLC1
                    DLC1 = file.readline()
                print("Game: Packa Pie DLC loaded.")
                time.sleep(0.5)
                      
        if ask_dlc.lower() in ["no", "n"]:
            return
        else:
            return

    @staticmethod
    def variables():
        #sets the variables to default values and creates them on startup or reset
        
        #general
        global username, day, rand_day, cash, level, exp, req_exp, shop, game_version, currency, supported_versions, rent, wages, day_name

        username = "Michael"
        shop = "Oh My Cod"
        day = 1
        rand_day = 0
        cash = 20
        level = 1
        exp = 0
        req_exp = 10
        game_version = "v1.4-beta"
        supported_versions = [""]
        currency = "£"
        rent = 10
        wages = 10
        day_name = 0
        
        #stock
        global cod, potato, sausage, fishcake, cooked_cod, cooked_potato, cooked_sausage, cooked_fishcake, cod_sellable, potato_sellable, sausage_sellable, fishcake_sellable
        
        cod = 12
        cooked_cod = 0
        cod_sellable = True
        
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
        global cod_cost, cooked_cod_cost, potato_cost, cooked_potato_cost, sausage_cost, cooked_sausage_cost, fishcake_cost, cooked_fishcake_cost
        
        cod_cost = 1
        cooked_cod_cost = 1.5
        
        potato_cost = 2
        cooked_potato_cost = 2.5
        
        sausage_cost = 3
        cooked_sausage_cost = 3.5

        fishcake_cost = 3
        cooked_fishcake_cost = 3.5 

        #exp values
        global cod_exp, potato_exp, sausage_exp, fishcake_exp

        cod_exp = 1
        potato_exp = 2
        sausage_exp = 3
        fishcake_exp = 3

        #fail/rand states
        global rand1, rand2, fail1, fail2

        rand1 = False
        rand2 = False
        fail1 = False
        fail2 = False

    @staticmethod
    def manager_name():
        #handles the username
        global username, yes_list, no_list
        username = input("Uncle Bob: Hello, I've forgotton your name. What was it again? ")
        #sets default if the input is blank
        if username == "":
            username = "Michael"
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
        global currency, yes_list, no_list
        
        print("Uncle Bob: Now we will move onto currency!")
        print("Uncle Bob: \n1. GBP/£ \n2. USD/$ \n3. EUR/€")
        ask_curr = input("Uncle Bob: Which currency would you like to use? ")
        if ask_curr in ["1"]:
            print("Uncle Bob: Ah the GBP! Good choice!")
            currency = "£"
            return
        elif ask_curr in ["2"]:
            print("Uncle Bob: Ah the USD! Good choice!")
            currency = "$"
            return
        elif ask_curr in ["3"]:
            print("Uncle Bob: Ah the EUR! Good choice!")
            currency = "€"
            return
        #else:
        #    print("Uncle Bob: Hm, that doesn't seem to be on the list!")
        #    GameInit.currency_name()

    @staticmethod  
    def startup():
        #sets up global varaibles used before GameInit.varibles()
        yes_list = ["yes", "y", "yes.", "y.", "yeah", "yh", "yeah.", "yh.", "hells yeah boi", "yeaah","yep", "yep."]
        no_list = ["no", "n", "no.", "n.", "nah", "noo", "nah.", "noo.", "hells nah boi", "naah", "nope", "nope."]
        x_loop = 1
        #runs all the startup stuff
        pre_init = input("Game: Hello, would you like to start a new game? ")
        pre_init = pre_init.lower()

        #skips the startup questions if the user is a tester
        if pre_init.lower() in ["default", "bug"]:
            GameInit.variables()
            GameMain.main()
            
        #runs the variable delcrations
        if pre_init in yes_list:
            #GameInit.check_dlc()
            GameInit.variables()
            #launches user-friendly text details
            launching = "Game: Launching"
            for x in range(3):
                launching = launching + "."
                print(launching)
                time.sleep(0.3)
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
        global level, cash, exp, req_exp, currency, day, yes_list, no_list, daytime
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
            GameInit.end()

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
        global yes_list, no_list, cod, cod_cost, potato, potato_cost, sausage, sausage_cost, fishcake, fishcake_cost, cash, level, currency, cash
        #asks the user if they want to buy stock to sell later on
        ask_stock = input("Fred: Would you like to buy some stock this morning (You have "+currency+ str(cash)+")? ")
        if ask_stock.lower() in yes_list:
            #shows how much stock they have and asks them what they want to buy
            print("Fred: Cod Stock: "+str(cod)+", Potato Stock: "+str(potato)+", Sasuage Stock: "+str(sausage)+" and Fishcake Stock: "+str(fishcake)+" ")
            ask_buy = input("Fred: What do you want to buy? ")
            
            #asks them how many fish they want to buy
            if ask_buy.lower() in ["cod", "cods", "c"]:
                item = cod
                item_name = "cod"
                item_cost = cod_cost
                
            #asks them how many potatoes they want to buy
            if ask_buy.lower() in ["potato", "potatoes", "potatos", "p"]:
                if level < 3:
                    print("Fred: Sorry! You need to be level 5 to unlock this!")
                    GameInit.buy_stock()
                elif level >= 3:
                    item = potato
                    item_name = "potato"
                    item_cost = potato_cost
                
            #asks them how many sausage they want to buy
            if ask_buy.lower() in ["sausage", "sausages", "s"]:
                #checks if the user is a high enough level to buy the stock to sell
                if level < 5:
                    print("Fred: Sorry! You need to be level 5 to unlock this!")
                    GameInit.buy_stock()
                elif level >= 5:
                    item = sausage
                    item_name = "sausage"
                    item_cost = sausage_cost
            
            #asks them how many fishcake they want to buy
            if ask_buy.lower() in ["fishcake", "fishcakes", "fc"]:
                #checks if the user is a high enough level to buy the stock to sell
                if level < 7:
                    print("Fred: Sorry! You need to be level 7 to unlock this!")
                    GameInit.buy_stock()
                elif level >= 7:
                    item = fishcake
                    item_name = "fishcake"
                    item_cost = fishcake_cost
                    
            #else:
            #    print("Fred: I'm not quite sure we sell that!")
            #    GameInit.buy_stock()

            def run_restock_function(item, item_name, item_cost):
                global cash
                
                ask_amount = int(input("Fred: How much "+str(item_name).capitalize()+" would you like to order? ("+currency + str(item_cost) + " a " + str(item_name) + ") "))
                if ask_amount > cash:
                    print("Fred: Sorry, we don't have the money to order that much!")
                    GameInit.buy_stock()
                    return
                else:
                    #adds the stock to the global var. and subtracts the cost
                    cash = cash - (ask_amount * item_cost)
                    item += int(ask_amount)
                    time.sleep(1.5)
                    return item, item_name

            item, item_name = run_restock_function(item, item_cost)
            if item_name == "cod":
                cod = item
            elif item_name == "potato":
                potato = item
            elif item_name == "sausage":
                sausage = item
            elif item_name == "fishcake":
                fishcake = item

            ask_reorder = input("Fred: Would you like to place another order? ")
            if ask_reorder in yes_list:
                GameInit.buy_stock()
            if ask_reorder in no_list:
                print("Fred: The order has arrived thanks to almost instant delivery!")
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
    def cook_all(food_name, food_num, food_cost):
        #variables
        global username, currency, level, yes_list, no_list, cooked_cod_cost
        #amount to cook
        print("Fred: How many "+food_name.lower()+" would you like to cook today? ")
        try:
            ask_cook = int(input("Fred: Just remember you only have "+str(food_num)+": "))
        except:
            print("Fred: You know thats not a number, right?")
            GameInit.cook_all()

        #stock check for cooking
        if int(ask_cook) > food_num:
            print("Fred: Boss, you can't cook more than you have!")
            GameInit.cook_all()
        else:
            print("Fred: I'll cook the "+food_name.lower()+" now Boss!")
            time.sleep(1.5)
            #subtracts the food and adds them to the cooked stock
            food_num = food_num - int(ask_cook)
            print("Fred: Okay Boss, the "+str(food_name)+" were cooked!")

        ask_change = input("Fred: Would you like to change the price today? ")
        if ask_change in ["yes", "y"]:
            food_cost = float(input("Fred: What would you like it to be? (Current: "+currency+str(food_cost)+") "))
            return ask_cook, food_cost
        if ask_change in ["no", "n"]:
            return ask_cook, food_cost

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
            print("Uncle Bob: It rained hard last night and a leak was found in the shop. You were charged "+currency+str(lesscash)+" to fix it!")
            cash -= lesscash
            print("Uncle Bob: You now have "+currency+str(cash)+" left!")
            rand1 == True

        #creates a random day number and runs the code if it is equal to the day and runs the stock spoiling event
        rand_day2 = randint(8, 13)
        if (rand_day2 == day) and (rand2 == False):
            print("-= Day "+str(rand_day)+": The Spoils =-")
            print("Uncle Bob: Somehow the fridge door was left open causing some of the stock to spoil.")
            cod = cod - rand_day
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
            print("Uncle Bob: Your Rick Harrison and that's no longer your paw-- fish and chip shop.")
        if username.lower() == "rick astley":
            print("Uncle Bob: Never gunna fry you up, never batter you down.")

        #checks if the variable(s) are below the threshold
        if cash > 0:
            print("Uncle Bob: You ran out of money, and the shop had to close. Try to mange your money better in the future.")
            fail1 == True
            game_version = "[FAILED]"
            return
        
        if cod > 0:
            print("Uncle Bob: You ran out of cod, and the shop had to close. Try to mange your cod better in the future.")
            fail2 == True
            game_version = "[FAILED]"
            return
        
    @staticmethod
    def stock_info():
        global yes_list, no_list
        #displays details on the current stock options
        ask_view = input("Fred: Would you like to view details on the stock? ")
        if ask_view.lower() in yes_list:
            print("Fred: Here's the stock book for you boss!")
            print("")
            #fish
            global cod_cost, cooked_cod_cost, cod_exp
            print("Book: Cod\n| Cod Cost: "+str(cod_cost)+" | Cooked Cod Cost: "+str(cooked_cod_cost)+" | Cod EXP: "+str(cod_exp)+" |")
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
            print("")

            time.sleep(5)
        if ask_view.lower() in no_list:
            return

    @staticmethod
    def manage_customers():
        global cooked_cod_cost, cooked_potato_cost, cooked_sausage_cost, cooked_fishcake_cost, level, hour_exp, tprofit
        global cod_customers, potato_customers, sausage_customers, fishcake_customers, cod_hour_exp, potato_hour_exp, sausage_hour_exp, fishcake_hour_exp
            
        #generates a random number using player level
        cod_rand_no = level * randint(1, 3)
            
        #checks if the price is low
        if cooked_cod_cost < 1:
            cod_rand_no = level * randint(1, 6)
        #checks if the price is good
        if 1 <= cooked_cod_cost <= 3:
            cod_rand_no = level * randint(1, 4)
        #checks if the price is high
        if 4 < cooked_cod_cost < 10:
            cod_rand_no = level * randint(1, 2)
        #checks if the price is unreasonable
        if cooked_cod_cost > 10:
            cod_rand_no = 0
            print("Uncle Bob: Those are some expensive cod, I'm not sure how many we will sell!")
                
        cod_customers = randint(0, cod_rand_no)
        cod_hour_exp = cod_customers * cod_exp

        #calculating the amount of customers and exp for potatoes
        if level >= 3:
            potato_rand_no = level * randint(1, 3)
                
            if cooked_potato_cost < 2:
                potato_rand_no = level * randint(1, 6)
            if 2 <= cooked_potato_cost <= 5:
                potato_rand_no = level * randint(1, 4)
            if 6 < cooked_potato_cost < 10:
                potato_rand_no = level * randint(1, 2)
            if cooked_potato_cost > 10:
                potato_rand_no = 0
                print("Uncle Bob: Those are some expensive chips!")
                    
            potato_customers = randint(0, potato_rand_no)
            potato_hour_exp = potato_customers * potato_exp

        #calculating the amount of customers and exp for sausage
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

        #calculating the amount of customers and exp for sausages
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

    @staticmethod
    def check_stock():
        global cooked_cod, cooked_potato, cooked_fishcake, level, cod_sellable, potato_sellable, sausage_sellable, fishcake_sellable
        global cod_customers, potato_customers, sausage_customers, fishcake_customers, tprofit
            
        if cod_customers > cooked_cod:
            print("Fred: Welp, we're out of cod!")
            cod_sellable = False
            if level < 3:
                return
                
        if (level >= 3) and (potato_customers > cooked_potato):
            print("Fred: Welp, we're out of chips!")
            potato_sellable = False
            if level < 5 and (cod_sellable == False):
                return

        if (level >= 5) and (sausage_customers > cooked_sausage):
            print("Fred: Welp, we're out of sausages!")
            sausage_sellable = False
            if level < 7 and (cod_sellable == False) and potato_sellable == False:
                return
                
        if (level >= 7) and (fishcake_customers > cooked_fishcake):
            print("Fred: Welp, we're out of fishcakes!")
            fishcake_sellable = False
            if (cod_sellable == False) and (potato_sellable == False) and (sausage_sellable == False):
                return
                
    @staticmethod
    def sell_stock():
        global cooked_cod, cooked_potato, cooked_fishcake, cooked_cod_cost, cooked_potato_cost, cooked_sausage_cost, cooked_fishcake_cost
        global level, cash, exp, req_exp, cod_sellable, potato_sellable, sausage_sellable, fishcake_sellable
        global cod_customers, potato_customers, sausage_customers, fishcake_customers, hour_exp, tprofit, cod_hour_exp, potato_hour_exp, sausage_hour_exp, fishcake_hour_exp
            
        #printing the sold fish and chips
        if cod_sellable == True:
            cooked_cod = cooked_cod - cod_customers
            cod_profit = cod_customers * cooked_cod_cost
            hour_exp = hour_exp + cod_hour_exp
            tprofit = tprofit + cod_profit
            
            if cod_customers == 0:
                print("Fred: No customers bought any cod.")
            if cod_customers > 0:
                 print("Fred: "+str(cod_customers)+" customers visted and ordered "+str(cod_customers)+" cod and we now have "+str(cooked_cod)+" cod left.")
            
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
            print(".")
            GameMain.generic_day()

    @staticmethod
    def generic_day():
        #global imports
        global cooked_cod, cooked_potato, cooked_fishcake, cooked_cod_cost, cooked_potato_cost, cooked_sausage_cost, cooked_fishcake_cost, cooked_haddock, haddock_sellable, cooked_haddock_cost, cooked_haddock_cost
        global level, cash, exp, req_exp, cod_sellable, potato_sellable, sausage_sellable, fishcake_sellable
        global cod, potato, sausage, fishcake, hour_exp, tprofit, daytime, username
        
        #start of day
        GameInit.random_days()
        GameInit.special_days()
        print("Fred: Good morning "+username+"!")
        GameInit.stock_info()
        GameInit.buy_stock()
        cooked_cod, cooked_cod_cost = GameInit.cook_all("Cod", cod, cooked_cod_cost)
        
        if level >= 3:
            cooked_potato, cooked_potato_cost = GameInit.cook_potato("Chips", potato, cooked_potato_cost)
        if level >= 5:
            cooked_sausage, cooked_sausage_cost = GameInit.cook_sausage("Sausage", sausage, cooked_sausage_cost)
        if level >= 7:
            cooked_fishcake, cooked_fishcake_cost = GameInit.cook_fishcake("Fishcake", fishcake, cooked_fishcake_cost)
            
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
        cod_customers = 0
        potato_customers = 0
        sausage_customers = 0
        fishcake_customers = 0
        cod_profit = 0
        potato_profit = 0
        sausage_profit = 0
        fishcake_profit = 0

        for daytime in range(0,6):
            #checking for the end of the day
            if fish_sellable == False:
                break
                
            #resetting variables
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
            
            #adds another hour
            daytime +=1
                
        GameInit.end()
        
            
class DataManage():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        global fail1, fail2, game_version
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
