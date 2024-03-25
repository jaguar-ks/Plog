from datetime import datetime
from colorama import Fore as cl
from colorama import Style as st

######################################################################
# A class representing a timer.
# 
# Attributes:
# - Hours: The number of hours on the timer.
# - Minutes: The number of minutes on the timer.
# - start: The start time of the timer.
# - lock: The time when the screen was locked.
# - apart: A boolean indicating if the screen is locked or not.
# - logTime: The total logged time on the timer.
# - timeAway: The total time away from the screen.
# - timeCtrlC: The total time when the program was interrupted.
# 
# Methods:
# - __init__(self, M): Initializes the timer with the given minutes.
# - __str__(self): Returns a string representation of the timer.
# - printHead(self): Prints the header of the timer.
# - screenLocked(self): Updates the timer when the screen is locked.
# - logedBack(self): Updates the timer when the screen is unlocked.
# - CrtlC(self): Updates the timer when the program is interrupted.
######################################################################

class Timer:

    Hours = Minutes = 0
    start = lock = datetime.now()
    apart = True
    logTime = timeAway = timeCtrlC = 0
        
    #################################################
    # Initializes the timer with the given minutes.
    # 
    # Parameters:
    # - M: The number of minutes to set on the timer.
    #################################################
    def __init__(self, M=0):
        if M >=60:
            self.Hours = M // 60
            self.Minutes = M % 60
        else:
            self.Minutes = M

    ##########################################################
    # Returns a string representation of the timer.
    # 
    # Returns:
    # - A string in the format "HH:MM" representing the timer.
    ##########################################################
    def __str__(self):
        Tm = str(self.Hours)
        if len(Tm) == 1:Tm = '0'+Tm
        Mn = str(self.Minutes)
        if len(Mn) == 1:Mn = '0'+Mn
        return Tm + ':' + Mn

    #################################
    # Prints the header of the timer.
    #################################
    def printHead(self):
        print(f'\t    {cl.BLUE}[StartTime {cl.CYAN}{Timer(self.start.hour * 60 + self.start.minute)}{cl.BLUE}]{st.RESET_ALL}')
        print(f"{cl.GREEN}_____________{cl.RED}______________{cl.MAGENTA}________________")
        print(f"{cl.GREEN}⎜[ LogTime ]⎥{cl.RED}⎥[ TimeAway ]⎥{cl.MAGENTA}⎥[ CurentTime ]⎥{st.RESET_ALL}")
        print(f"{cl.GREEN}⎜-----------⎥{cl.RED}⎥------------⎥{cl.MAGENTA}⎥--------------⎥")
    
    ##############################################
    # Updates the timer when the screen is locked.
    ##############################################
    def screenLocked(self):
        if self.apart == False:
            self.lock = datetime.now()
            self.logTime += abs((self.lock.hour * 60 + self.lock.minute) - (self.start.hour * 60 + self.start.minute))
            self.start = datetime.now()
            self.apart = True
    
    ################################################
    # Updates the timer when the screen is unlocked.
    ################################################
    def logedBack(self):
        if self.apart == True:
            curentTime = datetime.now()
            self.timeAway = abs((self.lock.hour * 60 + self.lock.minute) - (curentTime.hour * 60 + curentTime.minute))
            print(f'{cl.GREEN}⎜[  {cl.CYAN}{Timer(self.logTime)}  {cl.GREEN}]⎥{cl.RED}⎥[  {cl.CYAN}{Timer(self.timeAway)}   {cl.RED}]⎥{cl.MAGENTA}⎥[   {cl.CYAN}{Timer(curentTime.hour * 60 + curentTime.minute)}    {cl.MAGENTA}]⎥{st.RESET_ALL}')
            self.apart = False
    
    ####################################################
    # Updates the timer when the program is interrupted.
    ####################################################
    def CrtlC(self):
        curentTime = datetime.now()
        self.timeCtrlC = abs((self.lock.hour * 60 + self.lock.minute) - (curentTime.hour * 60 + curentTime.minute))
        print(f'\r{cl.GREEN}⎜[  {cl.CYAN}{Timer(self.logTime + self.timeCtrlC)}  {cl.GREEN}]⎥{cl.RED}⎥[  {cl.CYAN}{Timer(0)}   {cl.RED}]⎥{cl.MAGENTA}⎥[   {cl.CYAN}{Timer(datetime.now().hour * 60 + datetime.now().minute)}    {cl.MAGENTA}]⎥{st.RESET_ALL}')
        print(f"{cl.GREEN}⎣___________⎦{cl.RED}⎥____________⎦{cl.MAGENTA}⎥______________⎦")
        print(f"{cl.RED}exiting...{st.RESET_ALL}")