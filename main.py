#Shop Manager
import time, sys
from random import randint

class GameInit():
    #handles inital startup
    @staticmethod
    def variables():
        #general
        global day, rand_day, cash, level, exp, req_exp, total_customers, total_profit, shop

        shop = "The Shop"
        day = 1
        rand_day = 0
        cash = 30
        level = 1
        exp = 0
        req_exp = 10
        total_customers = 0
        total_profit = 0
        
        #stock
        global fish, potato, sausage, cooked_fish, cooked_potato, cooked_sausage, fish_sellable, potato_sellable, sausage_sellable
        
        fish = 20
        cooked_fish = 0
        potato = 0
        cooked_potato = 0
        sausage = 0
        cooked_sausage = 0
        fish_sellable = True
        potato_sellable = True
        sausage_sellable = True

        #prices
        global fish_cost, cooked_fish_cost, potato_cost, cooked_potato_cost
        
        fish_cost = 1
        cooked_fish_cost = 2
        potato_cost = 2
        cooked_potato_cost = 3
        sausage_cost = 3
        cooked_sausage_cost = 4        

        #exp values
        global fish_exp, potato_exp, sausage_exp

        fish_exp = 1
        potato_exp = 2

        #fail/rand states
        global rand1, fail1

        rand1 = False
        fail1 = False
    
    @staticmethod
    def manager_name():
        #handles the username
        global username
        username = input("Uncle Bob: What is your name, I always forget... ")
        username_ch = input("Uncle Bob: Just to check, your name is "+username+" right? ")
        if username_ch.lower() in ["yes", "y"]:
            return
        if username_ch.lower() in ["no", "n"]:
            GameInit.manager_name()
            return
        else:
            print("Game: Please enter a valid reply.")
            GameInit.manager_name()

    @staticmethod
    def shop_name():
        #handles the shop
        global shop
        shop = input("Uncle Bob: What would you like to shop to be renamed to? ")
        shop_ch = input("Uncle Bob: You want it called "+shop+"? ")
        if shop_ch.lower() in ["yes", "y"]:
            return
        if shop_ch.lower() in ["no", "n"]:
            GameInit.shop_name()
            return
        else:
            print("Game: Please enter a valid reply.")
            GameInit.shop_name()


    @staticmethod  
    def startup():
        #runs all the startup stuff
        pre_init = input("Game: Would you like to start a new game? ")
        pre_init = pre_init.lower()
        
        if pre_init in ["yes", "y"]:
            GameInit.variables()
            GameInit.manager_name()
            GameInit.shop_name()
            GameMain.main()
            return
        if pre_init in ["no", "n"]:
            ask_load = input("Game: Would you like to load a previous game? ")
            if ask_load in ["yes", "y"]:
                SaveLoad.load()
                return
            if ask_load in ["no", "n"]:
                SaveLoad.game_quit()
                return
            else:
                print("Game: Please enter a valid reply.")
                GameInit.startup()
        else:
            print("Game: Please enter a valid reply.")
            GameInit.startup()
            
    @staticmethod
    def end():
        global cooked_fish, cooked_potato, fish_sellable, potato_sellable
        fish_sellable = True
        potato_sellable = True
        print("Fred: Congratulations Boss, you finished the day!")
        print("Fred: You made $"+str(total_profit)+". You now have made $"+str(cash)+" overall")
        print("Fred: You are level "+str(level)+" and have "+str(exp)+"/"+str(req_exp)+" EXP for the next level.")
        if (cooked_fish > 0) or (cooked_potato > 0):
            print("Fred: Sadly, all unsold food had to be thrown away.")
        daytime = 0
        global day
        day = day + 1
        ask_sav = input("Game: Would you like to save your game? ")
        ask_sav = ask_sav.lower()
        if ask_sav in ["yes", "y"]:
            SaveLoad.save()
        elif ask_sav in ["no", "n"]:
            print("")
        else:
            print("Game: Please enter a valid response!")
            
        ask_qui = input("Game: Would you like to quit your game? ")
        ask_qui = ask_qui.lower()
        if ask_qui in ["yes", "y"]:
            SaveLoad.game_quit()
            return
        elif ask_qui in ["no", "n"]:
            return
        else:
            print("Game: Please enter a valid response!")

    @staticmethod
    def buy_stock():
        global fish, fish_cost, potato, potato_cost, sausage, sausage_cost, cash, level

        ask_stock = input("Fred: Hey boss, would you like to buy some stock this morning (You have $"+ str(cash)+")? ")
        if ask_stock.lower() in ["yes", "y"]:
            ask_buy = input("Fred: What do you want to buy? Current: Fish Stock: "+str(fish)+", Potato Stock: "+str(potato)+" and Sasuage Stock "+str(sausage)+" ")
            #fish
            if ask_buy.lower() in ["fish", "f"]:
                ask_amount = int(input("Fred: How many Fish would you like to order? ($" + str(fish_cost) + " a fish) "))
                if ask_amount > cash:
                    print("Fred: Sorry, we don't have the money to order that much!")
                    GameInit.buy_stock()
                    return
                else:
                    cash = cash - (ask_amount * fish_cost)                
                    fish = fish + ask_amount
                    time.sleep(1.5)
                    print("Fred: The order has arrived thanks to Congo Prime and the almost instant delivery!")
                    return
                
            #potato
            if ask_buy.lower() in ["potato", "potatoes", "p"]:
                if level < 3:
                    print("Sorry! You need to be level 3 to unlock this!")
                    buy_stock()
                elif level >= 3:
                    ask_amount = int(input("Fred: How many potatoes would you like to order? ($" + str(potato_cost) + " a potato) "))
                    if ask_amount > cash:
                        print("Fred: Sorry, we don't have the money to order that many!")
                        buy_stock()
                        return
                    else:
                        cash = cash - (ask_amount * potato_cost)                
                        potato = potato + ask_amount
                        time.sleep(1.5)
                        print("Fred: The order has arrived thanks to Congo Prime and the almost instant delivery!")
                        return
            else:
                print("Game: Please enter a valid reply.")
                GameInit.buy_stock()
                
            #sausage
            if ask_buy.lower() in ["sausage", "sausages", "s"]:
                if level < 5:
                    print("Sorry! You need to be level 5 to unlock this!")
                    buy_stock()
                elif level >= 3:
                    ask_amount = int(input("Fred: How many sausages would you like to order? ($" + str(sausage_cost) + " a sausage) "))
                    if ask_amount > cash:
                        print("Fred: Sorry, we don't have the money to order that much!")
                        buy_stock()
                        return
                    else:
                        cash = cash - (ask_amount * sausage_cost)                
                        sausage = sausage + ask_amount
                        time.sleep(1.5)
                        print("Fred: The order has arrived thanks to Congo Prime and the almost instant delivery!")
                        return
            else:
                print("Game: Please enter a valid reply.")
                GameInit.buy_stock()
                
        if ask_stock.lower() in ["no", "n"]:
            print("Fred: We can always order more tomorrow if we need.")
            return
        
        else:
            print("Game: Please enter a valid reply.")
            GameInit.buy_stock()
            
    @staticmethod
    def cook_fish():
        #variables
        global username, fish, cooked_fish, level, cooked_fish_cost

        #fish
        print("Fred: Perfect! How many fish do you want to cook this morning? ")
        ask_fish = int(input("Fred: Lastly "+username+", you only have "+str(fish)+": "))
        if ask_fish > fish:
            print("Fred: Boss, you can't cook more than you have!")
            GameInit.cook_stock()
        else:
            print("Fred: I'll cook the fish now Boss!")    
            time.sleep(1.5)
            fish = fish - ask_fish
            cooked_fish = ask_fish
            print("Fred: Al'ight Boss, "+str(cooked_fish)+" fish were cooked!")
        
        ask_chg = input("Fred: Would you like to change the price today? ")
        if ask_chg in ["yes", "y"]:
            cooked_fish_cost = float(input("Fred: What would you like it to be? (Current: $"+str(cooked_fish_cost)+") "))
            return
        if ask_chg in ["no", "n"]:
            print("Fred: Okay "+username)
            return

    @staticmethod
    def cook_potato():
        #variables
        global potato, cooked_potato, level, potato_sellable, username, cooked_potato_cost
        #potato
        ask_pots = input("Fred: Would you like to cook chips today? ")
        if ask_pots.lower() in ["yes", "y"]:
            print("Fred: Sounds great! How many potatoes do you want to cook this morning? ")
            ask_potato = int(input("Fred: By the way, you currently have "+str(potato)+": "))
            if ask_potato > potato:
                print("Fred: Boss, you can't cook more than you have!")
                cook_stock()    
            else:
                print("Fred: I'll cook the potatoes now Boss!")
                time.sleep(1.5)
                potato = potato - ask_potato
                cooked_potato = ask_potato
                print("Fred: Al'ight Boss, "+str(cooked_potato)+" portions of chips were cooked!")
            
        if ask_pots.lower() in ["no", "n"]:
            potato_sellable = False
            print("Fred: Okay boss.")

        ask_chg = input("Fred: Would you like to change the price today? ")
        if ask_chg in ["yes", "y"]:
            cooked_potato_cost = float(input("Fred: What would you like it to be? (Current: $"+str(cooked_potato_cost)+") "))
            return
        if ask_chg in ["no", "n"]:
            print("Fred: Okay "+username)
            return

    @staticmethod
    def cook_sausage():
        #variables
        global sausage, cooked_sausage, level, sausage_sellable, username, cooked_sausage_cost
        #potato
        ask_pots = input("Fred: Would you like to cook sauages today? ")
        if ask_pots.lower() in ["yes", "y"]:
            print("Fred: Sounds great! How many sausages do you want to cook this morning? ")
            ask_potato = int(input("Fred: You have "+str(sausages)+": "))
            if ask_potato > potato:
                print("Fred: Boss, you can't cook more than you have!")
                cook_stock()    
            else:
                print("Fred: I'll cook the sausages now Boss!")
                time.sleep(1.5)
                potato = potato - ask_sausages
                cooked_sausage = ask_sausages
                print("Fred: Al'ight Boss, "+str(cooked_potato)+" portions of chips were cooked!")
            
        if ask_pots.lower() in ["no", "n"]:
            sausage_sellable = False
            print("Fred: Okay boss.")

        ask_chg = input("Fred: Would you like to change the price today? ")
        if ask_chg in ["yes", "y"]:
            cooked_sausage_cost = float(input("Fred: What would you like it to be? (Current: $"+str(cooked_sausage_cost)+") "))
            return
        if ask_chg in ["no", "n"]:
            print("Fred: Okay "+username)
            return

    @staticmethod
    def special_days():
        #special days
        global cash, day, shop
        if day == 1:
            print("-= Day 1: The Beginning =-")
            print("Uncle Bob: Welcome to ShopManager "+username+"! You must run "+shop+" inherited from me, your Uncle Bob!")
            time.sleep(1.5)
        
        if day == 7:
            print("-= Day 7: The First Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra $50 to get you on your way!")
            cash = cash + 50
            print("Game: You now have $"+str(cash)+"!")
            time.sleep(1.5)

        if day == 14:
            print("-= Day 14: The Second Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through a second week. Impressive! Here's an extra $100 to get you on your way!")
            cash = cash + 100
            print("Game: You now have $"+str(cash)+"!")
            time.sleep(1.5)

        
        elif day not in [1, 7, 14, rand_day]:
            print("-= Day "+str(day)+" =-")
            time.sleep(1.5)
        else:
            return

    @staticmethod
    def random_days():
        global day, rand_day, rand1, cash
        #picks a random day and runs a special feature
        rand_day = randint(2, 6)
        if (rand_day == day) and (rand1 == False):
            print("-= Day "+str(rand_day)+": The Leak =-")
            print("Uncle Bob: It rained hard last night and a leak was found in the shop. You were charged $10 to fix it!")
            cash = cash - 10
            print("Uncle Bob: You now have $"+str(cash)+" left!")
            rand1 == True

    @staticmethod
    def game_over():
        #manages the game over state
        global username, fail1
        if username == "Hudson":
            print("Uncle Bob: It's gamer over man, game over!")
        if cash > 0:
            print("Uncle Bob: You ran out of money, and the shop had to close. Try to mange your money better in the future.")
            fail1 == True
            SaveLoad.save()
            return

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("")
            GameMain.generic_day()

    @staticmethod
    def generic_day():
        #global imports
        global level, cooked_fish, cooked_potato, cooked_fish_cost, cooked_potato_cost, total_customers, total_profit, cash, exp, req_exp, fish_sellable, potato_sellable, sausage_sellable
                
        #start of day
        GameInit.random_days()
        GameInit.special_days()
        GameInit.buy_stock()
        GameInit.cook_fish()
        if level >= 3:
            GameInit.cook_potato()
        if level >= 5:
                GameInit.cook_sausage()
        
        #middle section of day
        print("Fred: Well "+username+", we'd better open up for the day.")
        profit = 0
        daytime = 0
        potato_customers = 0
        sausage_customers = 0
        potato_profit = 0
        sausage_profit = 0

        while True:
            #checking if the the daytime is past 9pm
            if daytime >= 7:
                GameInit.end()
                return
                
            #printing the current time of day
            print("Game: "+str((daytime + 3))+":00pm")
            time.sleep(2)

            #calculaing the amount of customers and exp
            fish_rand_no = level * randint(1, 3)
            
            if cooked_fish_cost < 1:
                fish_rand_no = level * randint(1, 6)
            if 1 <= cooked_potato_cost <= 3:
                fish_rand_no = level * randint(1, 4)
            if 4 < cooked_fish_cost < 10:
                fish_rand_no = level * randint(1, 2)
            if cooked_fish_cost > 10:
                fish_rand_no = 0
                print("Uncle Bob: Those are some expensive fish!")
                
            fish_customers = randint(0, fish_rand_no)
            fish_hour_exp = fish_customers * fish_exp

            if level >= 3:
                potato_rand_no = level * randint(1, 3)
                
                if cooked_potato_cost < 2:
                    potato_rand_no = level * randint(1, 6)
                if 2 <= cooked_potato_cost <= 5:
                    potato_rand_no = level * randint(1, 4)
                if 6 < cooked_fish_cost < 10:
                    fish_rand_no = level * randint(1, 2)
                if cooked_fish_cost > 10:
                    fish_rand_no = 0
                    print("Uncle Bob: Those are some expensive chips!")
                    
                potato_customers = randint(0, potato_rand_no)
                potato_hour_exp = potato_customers * potato_exp

            if level >= 5:
                sausage_rand_no = level * randint(1, 3)
                
                if cooked_sausage_cost < 3:
                    sausage_rand_no = level * randint(1, 6)
                if 3 <= cooked_sausage_cost <= 7:
                    sausage_rand_no = level * randint(1, 4)
                if 8 < cooked_sausage_cost < 11:
                    sausage_rand_no = level * randint(1, 2)
                if cooked_sausage_cost > 12:
                    fish_rand_no = 0
                    print("Uncle Bob: Those are some expensive sausages!")
                    
                sausage_customers = randint(0, sausage_rand_no)
                sausage_hour_exp = sausage_customers * sausage_exp
                
            #checking if there is stock left
            if fish_customers > cooked_fish:
                print("Fred: Welp, we're out of fish!")
                fish_sellable = False
                if not level >= 3:
                    GameInit.end()
                    return
                
            if (level >= 3) and (potato_customers > cooked_potato):
                print("Fred: Welp, we're out of chips!")
                potato_sellable = False

            if (level >= 5) and (sausage_customers > sausage_potato):
                print("Fred: Welp, we're out of sausages!")
                sausage_sellable = False
                
            if (fish_sellable == False) and (potato_sellable == False) and (sausage_sellable == False):
                GameInit.end()

            #printing the sold fish and chips
            if fish_sellable == True:
                cooked_fish = cooked_fish - fish_customers
                fish_profit = fish_customers * cooked_fish_cost
                hour_exp = fish_hour_exp
            
                if fish_customers == 0:
                    print("Fred: No customers bought any fish.")
                if fish_customers > 0:
                    print("Fred: "+str(fish_customers)+" customers visted and ordered "+str(fish_customers)+" fish and we now have "+str(cooked_fish)+" fish left.")
            
            if level >= 3 and potato_sellable == True:
                cooked_potato = cooked_potato - potato_customers
                potato_profit = potato_customers * cooked_potato_cost
                hour_exp = hour_exp + potato_hour_exp
                
                if potato_customers == 0:
                    print("Fred: No customers bought any chips.")
                if potato_customers > 0:
                    print("Fred: "+str(potato_customers)+" customers bought "+str(potato_customers)+" portions of chips and we now have "+str(cooked_potato)+" portions left!")

            if level >= 5 and sausage_sellable == True:
                cooked_sausage = cooked_sausage - sausage_customers
                sausage_profit = sausage_customers * cooked_sausage_cost
                hour_exp = hour_exp + sausage_hour_exp
                
                if sausage_customers == 0:
                    print("Fred: No customers bought any chips.")
                if sausage_customers > 0:
                    print("Fred: "+str(sausage_customers)+" customers bought "+str(sausage_customers)+" sausages and we now have "+str(cooked_sausage)+" sausages left!")

            #calculating the profits, exp and cash for the day
            profit = fish_profit + potato_profit + sausage_profit
            cash = cash + profit
            exp = exp + hour_exp
            print("Fred: From this, you've made $"+str(profit)+" and gained "+str(hour_exp)+" EXP.")

            #checking if the user meets the requirements for a level up
            if exp >= req_exp:
                level = level + 1
                exp = exp - req_exp
                req_exp = req_exp * 2
                print("Uncle Bob: Congratulations! You levelled up to "+str(level)+"!")
                print("Uncle Bob: With this, your reputation has increased.")

            #checking for the end of the day using var 'daytime'
            if daytime >= 7:
                if (fish_sellable == False) and (potato_sellable == False):
                    return
                GameInit.end()
                GameInit.game_over()
                if fail1 == True:
                    sys.exit() 
            else:
                daytime = daytime + 1
            
class SaveLoad():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        global fail1
        save_name = input("Game: What would you like the save file to be called? ")
        print("Game: Saving Game...")
        file = open(save_name+".shs", "w")
        file.write(username)
        file.write("\n")
        file.write(str(day))
        file.write("\n")
        file.write(str(level))
        file.write("\n")
        file.write(str(cash))
        file.write("\n")
        file.write(str(fish))
        file.write("\n")
        file.write(str(potato))
        file.write("\n")
        file.write(str(exp))
        file.write("\n")
        file.write(str(req_exp))
        file.write("\n")
        file.write(shop)
        file.write("\n")
        file.write(str(sausage))
        file.write("\n")
        if fail1 == True:
            file.write("Failed: Out of Cash")
            file.write("\n")
            
        print("Game: Game Saved!")


    @staticmethod
    def load():
        #handles game loading
        save_name = input("Game: What is the name of the save file? ")
        print("Game: Loading Game...")
        GameInit.variables()

        global username, day, level, cash, fish, potato, exp, req_exp
        
        file = open(save_name+".shs", "r")
        #username
        username = file.readline().replace("\n", "")

        #day
        day = int(file.readline().replace("\n", ""))

        #level
        level = int(file.readline().replace("\n", ""))

        #cash
        cash = float(file.readline().replace("\n", ""))

        #fish
        fish = int(file.readline().replace("\n", ""))
        
        #potato
        potato = int(file.readline().replace("\n", ""))

        #exp
        exp = int(file.readline().replace("\n", ""))

        #req_exp
        req_exp = int(file.readline().replace("\n", ""))
        
        #shop
        shop = file.readline().replace("\n", "")

        #sausage
        sausage = int(file.readline().replace("\n", ""))

        print("Game: Game Loaded!")
        GameMain.main()

    def game_quit():
        ask_quit = input("Game: Are you sure? ")
        if ask_quit in ["yes", "y"]:
            print("\n \n \n")
            GameInit.variables()
            GameInit.startup()
        if ask_quit in ["no", "n"]:
            return
        
GameInit.startup()
