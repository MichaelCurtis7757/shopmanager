#Shop Manager
import time

class GameInit():
    #handles inital startup
    def variables():
        #general
        global day
        global cash
        
        day = 1
        cash = 0
        
        #stock
        global fish
        global potato
        
        fish = 50
        cooked_fish = 0
        potato = 50
        cooked_potato = 0
    
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

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("Game: Starting Game...\n")
            GameMain.generic_day()
            break

    def generic_day():
        #special days
        if day == 1:
            print("-= Day 1: The Beginning =-")
            print("Uncle Bob: Welcome to ShopManager! You must run the shop inherited from me, your Uncle Bob!")
            time.sleep(1.5)
        
        if day == 7:
            print("-= Day 7: The First Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra $250 to get you on your way!")
            cash = cash + 250
            time.sleep(1.5)
        
        elif not (day == 1) or (day == 7):
            print("-= Day "+str(day)+" =-")
            time.sleep(1.5)
        
        #start of day
        def fish_check():
            global fish
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

        #end of day
        print("Fred: Congratulations Boss, you finished the day!")
        print("Fred: Sadly, all unsold food has to be thrown away.")
        global day
        day = day + 1
        def end():
            ask_sav = input("Game: Would you like to save your game? ")
            ask_sav = ask_sav.lower()
            if ask_sav in ["yes", "y"]:
                SaveLoad.save()
                return
            elif ask_sav in ["no", "n"]:
                return
            else:
                print("Game: Please enter a valid response!")
        end()
        
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
