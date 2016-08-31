#Shop Manager

class GameInit():
    #handles inital startup
    @staticmethod
    def manager_name():
        #handles the username   
        username = input("What is your name? ")
        username_ch = input("Just to check, your name is '"+username+"', right? ")
            
        if username_ch in ["yes", "y"]:
            return
        
        if username_ch in ["no", "n"]:
            SGameInit.manager_name()
        else:
            print("Please enter a valid response!")
            GameInit.manager_name()

    @staticmethod  
    def startup():
        #runs all the startup stuff
        pre_init = input("Would you like to start a new game? ")
        pre_init = pre_init.lower()
        
        if pre_init in ["yes", "y"]:
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
    
class SaveLoad():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        print("console: loaded save func.")

    @staticmethod
    def load():
        #handles game loading
        print("console: loaded load func.")

GameInit.startup()
