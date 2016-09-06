#Shop Manager
import time
from random import randint

class GameInit():
    #handles inital startup
    @staticmethod
    def variables():
        #general
        global day
        global cash
        global level
        global exp
        global req_exp
        global total_customers
        global total_profit
        
        day = 1
        cash = 50
        level = 1
        exp = 0
        req_exp = 10
        total_customers = 0
        total_profit = 0
        
        #stock
        global fish
        global potato
        global cooked_fish
        global cooked_potato
        
        fish = 20
        cooked_fish = 0
        potato = 20
        cooked_potato = 0

        #prices
        global fish_cost
        global cooked_fish_cost
        global potato_cost
        global cooked_potato_cost
        
        fish_cost = 1
        cooked_fish_cost = 2
        potato_cost = 2
        cooked_potato_cost = 2

        #exp values
        global fish_exp

        fish_exp = 1
    
    @staticmethod
    def manager_name():
        #handles the username
        global username
        username = input("Uncle Bob: What is your name, I always forget... ")
        username_ch = input("Uncle Bob: Just to check, your name is "+username+", right? ")
        username_ch = username_ch.lower()
        if username_ch in ["yes", "y"]:
            return
        if username_ch in ["no", "n"]:
            GameInit.manager_name()
            return
        else:
            print("Game: Please enter a valid response!")
            GameInit.manager_name()

    @staticmethod  
    def startup():
        #runs all the startup stuff
        pre_init = input("Game: Would you like to start a new game? ")
        pre_init = pre_init.lower()
        
        if pre_init in ["yes", "y"]:
            GameInit.variables()
            GameInit.manager_name()
            GameMain.main()
            return
        if pre_init in ["no", "n"]:
            SaveLoad.load()
            return
        else:
            print("Game: Please enter a valid response!")
            GameInit.startup()

    @staticmethod
    def end():
        print("Fred: Congratulations Boss, you finished the day!")
        print("Fred: You sold "+str(total_customers)+" cooked fish and made $"+str(total_profit)+". You now have made $"+str(cash)+" overall")
        print("Fred: You are level "+str(level)+" and have "+str(exp)+"/"+str(req_exp)+" EXP for the next level.")
        print("Fred: Sadly, all unsold food had to be thrown away.")
        daytime = 0
        global day
        day = day + 1
        ask_sav = input("Game: Would you like to save your game? ")
        ask_sav = ask_sav.lower()
        if ask_sav in ["yes", "y"]:
            SaveLoad.save()
            return
        elif ask_sav in ["no", "n"]:
            return
        else:
            print("Game: Please enter a valid response!")

    @staticmethod
    def buy_stock():
        global fish
        global fish_cost
        global cash

        ask_stock = input("Fred: Hey boss, would you like to buy some stock this morning? You have $"+ str(cash) + " and " + str(fish) + " fish. ")
        if ask_stock.lower() in ["yes", "y"]:
            ask_buy = input("Fred: Okay boss, would you like to buy some 'Fish' or 'Potatoes'? ")
            if ask_buy.lower() in ["fish", "f"]:
                ask_amount = int(input("Fred: How many Fish would you like to order? ($" + str(fish_cost) + " a fish) "))
                if ask_amount > cash:
                    print("Fred: Sorry, we don't have the money to order that much!")
                    buy_stock()
                    return
                else:
                    cash = cash - (ask_amount * fish_cost)                
                    fish = fish + ask_amount
                    print("Fred: The order has arrived thanks to Congo Prime and it's instant delivery!")
                    return
            if ask_buy.lower() in ["potato", "potatoes", "p"]:
                #future update stuff
                return
        if ask_stock.lower() in ["no", "n"]:
            print("Fred: We can always order more tomorrow if we need.")
            return
            
    @staticmethod
    def cook_stock():
        #variables
        global fish
        global cooked_fish

        #fish
        print("Fred: Sounds good! How many fish do you want to cook this morning? ")
        ask_fish = int(input("Fred: Oh, you currently have "+str(fish)+": "))
        if ask_fish > potato:
            print("Fred: Boss, you can't cook more than you have!")
            fish_check()
            return
        else:
            print("Fred: I'll cook the fish now Boss!")
            time.sleep(1.5)
            fish = fish - ask_fish
            cooked_fish = ask_fish
            print("Fred: Al'ight Boss, "+str(cooked_fish)+" were cooked!")

        #potato

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("")
            GameMain.generic_day()

    @staticmethod
    def generic_day():
        #special days
        if day == 1:
            print("-= Day 1: The Beginning =-")
            print("Uncle Bob: Welcome to ShopManager! You must run the shop inherited from me, your Uncle Bob!")
            time.sleep(1.5)
        
        if day == 7:
            print("-= Day 7: The First Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra $50 to get you on your way!")
            global cash
            cash = cash + 50
            print("Game: You now have $"+str(cash)+"!")
            time.sleep(1.5)
        
        elif not (day == 1) or (day == 7):
            print("-= Day "+str(day)+" =-")
            time.sleep(1.5)

        #start of day
        GameInit.buy_stock()
        GameInit.cook_stock()
        
        #middle section of day
        print("Fred: Well boss, we'd better open up for the day.")
        daytime = 0

        while True:
            #time prints
            if daytime == 0:
                print("Game: 3:00pm")
            if daytime == 1:
                print("Game: 4:00pm")
            if daytime == 2:
                print("Game: 5:00pm")
            if daytime == 3:
                print("Game: 6:00pm")
            if daytime == 4:
                print("Game: 7:00pm")
            if daytime == 5:
                print("Game: 8:00pm")
            if daytime == 6:
                print("Game: 9:00pm")

            time.sleep(1.5)

            #customers entering
            global level
            rand_no = level * randint(1, 3)
            customers = randint(0, rand_no)
            hour_exp = customers * fish_exp

            #fish check
            global cooked_fish
            if customers > cooked_fish:
                print("Fred: Welp, we're out of fish!")
                GameInit.end()
                return

            global cooked_fish_cost
            cooked_fish = cooked_fish - customers
            profit = customers * cooked_fish_cost

            
            if customers == 0:
                print("Fred: "+str(customers)+" customers have come in. Gosh darn'it!")
            
            else:
                print("Fred: "+str(customers)+" customers have come in. They ordered "+str(customers)+" cooked fish and we now have "+str(cooked_fish)+" cooked fish left!")
                print("Fred: From this, you've made $"+str(profit)+" and gained "+str(hour_exp)+" EXP.")

            #managing totals
            global total_customers
            total_customers = total_customers + customers
            global total_profit
            total_profit = total_profit + profit

            global cash
            cash = cash + profit
            global exp
            exp = exp + hour_exp

            #run level check
            global exp
            global req_exp
            global level
        
            if exp == req_exp:
                level = level + 1
                exp = exp - req_exp
                req_exp = req_exp * 2
                print("Uncle Bob: Congratulations! You levelled up to "+str(level)+"!")
            
                if daytime == 6:           
                    #end of day
                    GameInit.end()
                    return
                
            daytime = daytime + 1
            
class SaveLoad():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        save_name = input("Game: What would you like the save file to be called? ")
        print("Game: Saving Game...")
        file = open(save_name+".txt", "w")
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
        print("Game: Game Saved!")

    @staticmethod
    def load():
        #handles game loading
        print("Game: Loading Game...")
        save_name = input("Game: What is the name of the save file? ")
        GameInit.variables()

        file = open(save_name+".txt", "r")
        #username
        load_username = file.readline().replace("\n", "")
        global username
        username = load_username

        #day
        load_day = file.readline().replace("\n", "")
        global day
        day = int(load_day)

        #level
        load_level = file.readline().replace("\n", "")
        global level
        level = int(load_level)

        #cash
        load_cash = file.readline().replace("\n", "")
        global cash
        cash = int(load_cash)

        #fish
        load_fish = file.readline().replace("\n", "")
        global fish
        fish = int(load_fish)
        
        #potato
        load_potato = file.readline().replace("\n", "")
        global potato
        potato = int(load_potato)

        #exp
        load_exp = file.readline().replace("\n", "")
        global exp
        exp = int(load_exp)

        #req_exp
        load_req_exp = file.readline().replace("\n", "")
        global req_exp
        req_exp = int(load_req_exp)

        print("Game: Game Loaded!")
        GameMain.main()
        
GameInit.startup()
