#Shop Manager

class GameInit():
    #handles inital startup
    def manager_name():
        #handles the username
        while True:    
            username = input("What is your name? ")
            username_ch = input("Just to check, your name is '"+username+"', right? ")
            
            if (username_ch == "y") or (username_ch == "yes"):
                break
            
            if (username_ch == "n") or (username_ch == "no"):
                GameInit.manager_name()
        
    def startup():
        #
        pre_init = input("Would you like to start a new game? ")
        pre_init = pre_init.lower()
        
        if (pre_init == "y") or (pre_init == "yes"):
            print("console: input is yes")
            GameInit.manager_name()
            GameMain.main()
            return
        if (pre_init == "n") or (pre_init == "no"):
            print("console: input is no")
            return
        else:
            print("console: error, restarting check")
            GameInit.startup()          

class GameMain():
    #handles the main game
    def main():
        while True:
            print("console: game started successfully")
            break
    
class SaveLoad():
    #handles the save/load functions
    def save():
        #handles game saving
        print("console: loaded save func.")
        
    def load():
        #handles game loading
        print("console: loaded load func.")

GameInit.startup()
