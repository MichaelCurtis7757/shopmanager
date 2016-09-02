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
        global total_customers
        global total_profit
        
        day = 1
        cash = 50
        level = 1
        total_customers = 0
        total_profit = 0
        
        #stock
        global fish
        global potato
        global cooked_fish
        global cooked_potato
        
        fish = 50
        cooked_fish = 0
        potato = 50
        cooked_potato = 0

        #prices
        global fish_cost
        global cooked_fish_cost
        
        fish_cost = 1
        cooked_fish_cost = 2
    
    @staticmethod
    def manager_name():
        #handles the username
        global username
        username = input("Uncle Bob: What is your name, I always forget... ")
        username_ch = input("Uncle Bob: Just to check, your name is '"+username+"', right? ")
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
        print("Fred: You sold "+str(total_customers)+" cooked fish and made $"+str(total_profit)+". You now have made $"+str(cash)+" overall.")
        print("Fred: Sadly, all unsold food has to be thrown away.")
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

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("\n")
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
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra $250 to get you on your way!")
            global cash
            cash = cash + 250
            print("Game: You now have $"+str(cash)+"!")
            time.sleep(1.5)
        
        elif not (day == 1) or (day == 7):
            print("-= Day "+str(day)+" =-")
            time.sleep(1.5)

        #start of day
        def fish_check():
            global fish
            global cooked_fish
            print("Fred: Mornin' Boss, how many fish do you want to cook this morning? ")
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
            
        fish_check()
        
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
                print("Fred: "+str(customers)+" have come in. Gosh darn'it!")
            
            else:
                print("Fred: "+str(customers)+" have come in. They ordered "+str(customers)+" cooked fish and we now have "+str(cooked_fish)+" cooked fish left!")
                print("Fred: From this, you've made $"+str(profit)+".")

            #managing totals
            global total_customers
            total_customers = total_customers + customers
            global total_profit
            total_profit = total_profit + profit
            
            if daytime == 6:           
                #end of day
                global cash
                cash = cash + total_profit
                GameInit.end()
                return
            daytime = daytime + 1
        
class SaveLoad():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        print("Game: Saving Game...")
        file = open("data.txt", "w")
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
        print("Game: Game Saved!")

    @staticmethod
    def load():
        #handles game loading
        print("Game: Loading Game...")

        file = open("data.txt", "r")
        #username
        load_username = file.readline().replace("\n", "")
        username = load_username

        #day
        load_day = file.readline().replace("\n", "")
        day = load_day

        #level
        load_level = file.readline().replace("\n", "")
        level = load_level

        #cash
        load_cash = file.readline().replace("\n", "")
        cash = load_cash

        #fish
        load_fish = file.readline().replace("\n", "")
        fish = load_fish
        
        #potato
        load_potato = file.readline().replace("\n", "")
        potato = load_potato

        print("Game: Game Loaded!")
        
GameInit.startup()
