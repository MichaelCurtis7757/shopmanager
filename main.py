#Shop Manager

class GameInit():
    #handles inital startup
    def variables():
        #general
        global day, cash, fish, potato
        day = 1
        cash = 0
        
        #stock
        fish = 0
        cooked_fish = 0
        potato = 0
        cooked_potato = 0
    
    @staticmethod
    def manager_name():
        #handles the username
        global username
        username = input("What is your name? ")
        username_ch = input("Just to check, your name is '"+username+"', right? ")
            
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
            return
        else:
            print("Please enter a valid response!")
            GameInit.startup()          

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("console: game started successfully")
            break

    def generic_day():
        #start of day
        if day == 1:
            print("Welcome to your first day, let's hope it's a good one!")
            
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
        print("console: loaded load func.")

GameInit.startup()
