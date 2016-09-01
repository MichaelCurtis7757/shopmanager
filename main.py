#Shop Manager

class GameInit():
    #handles inital startup
    def variables():
        #general
        global day, cash, fish, potato
        day = 1
        cash = 0
        
        #stock
        fish = 50
        cooked_fish = 0
        potato = 50
        cooked_potato = 0
    
    @staticmethod
    def manager_name():
        #handles the username
        global username
        username = input("What is your name? ")
        username_ch = input("Just to check, your name is '"+username+"', right? ")
        username_ch = username_ch.lower()
        if username_ch in ["yes", "y"]:
            return
        if username_ch in ["no", "n"]:
            GameInit.manager_name()
            return
        else:
            print("Please enter a valid response!")
            GameInit.manager_name()

    @staticmethod  
    def startup():
        #runs all the startup stuff
        pre_init = input("Would you like to start a new game? ")
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
            print("Please enter a valid response!")
            GameInit.startup()          

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("Starting Game...")
            GameMain.generic_day()
            break

    def special_days():
        #special day stuff
        if day == 1:
            print("-= Day 1: The Beginning =-")
            print("Uncle Bob: Welcome to ShopManager! You must run the shop inherited from me, your Uncle Bob!")
            return
        
        if day == 7:
            print("-= Day 7: The First Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra $250 to get you on your way!")
            #day 7 cash bonus
            cash = cash + 250
            return

    def generic_day():
        #start of day
        def fish_check():
            print("Fred: Mornin' Boss, how many fish do you want to cook this morning? ")
            ask_fish = input("Fred: Oh, you currently have "+str(fish)+": ")
            if ask_fish > potato:
                print("Fred: Boss, you can't cook more than you have!")
                fish_check()
                return
            else:
                return
        
        #middle section of day

        #end of day
        print("Congratulations, you finished the day!")
        def end():
            ask_sav = input("Would you like to save your game? ")
            ask_sav = ask_sav.lower()
            if ask_sav in ["yes", "y"]:
                return
            elif ask_sav in ["no", "n"]:
                return
            else:
                print("Please enter a valid response!")
        end()
        
class SaveLoad():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        print("Saving Game...")
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
        print("Game Saved!")

    @staticmethod
    def load():
        #handles game loading
        print("Loading Game...")

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

        #temp code below
        print(load_data)
        
GameInit.startup()
