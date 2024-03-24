from datetime import datetime
from colorama import Fore as cl
from colorama import Style as st

"""
A class representing a timer.

Attributes:
    Hours (int): The number of hours on the timer.
    Minutes (int): The number of minutes on the timer.

Methods:
    __init__(self, M=0): Initializes the Timer object with the given number of minutes.
    __str__(self): Returns a string representation of the timer in the format 'HH:MM'.
"""
class Timer:
    Hours = Minutes = 0
    start = lock = datetime.now()
    apart = True
    logTime = timeAway = timeCtrlC = 0
        
    def __init__(self, M=0):
        if M >=60:
            self.Hours = M // 60
            self.Minutes = M % 60
        else:
            self.Minutes = M

    def __str__(self):
        Tm = str(self.Hours)
        if len(Tm) == 1:Tm = '0'+Tm
        Mn = str(self.Minutes)
        if len(Mn) == 1:Mn = '0'+Mn
        return Tm + ':' + Mn

    def printHead(self):
        print(f'      {cl.BLUE}[StartTime {cl.CYAN}{Timer(self.start.minute)}{cl.BLUE}]{st.RESET_ALL}')
        print(f"{cl.GREEN}[LogTime]{cl.RED}[TimeAway]{cl.MAGENTA}[CurentTime]{st.RESET_ALL}")
    
    def screenLocked(self):
        if self.apart == False:
            self.lock = datetime.now()
            self.logTime += ((self.lock.hour - self.start.hour) * 60) + (self.lock.minute - self.start.minute)
            self.timeCtrlC = ((self.lock.hour - self.start.hour) * 60) + (self.lock.minute - self.start.minute)
            self.start = datetime.time()
            self.apart = True
    
    def logedBack(self):
        if self.apart == True:
            curentTime = datetime.now()
            self.timeAway = curentTime.minute - self.lock.minute
            print(f'{cl.GREEN}[ {cl.CYAN}{Timer(self.logTime)} {cl.GREEN}]{cl.RED}[ {cl.CYAN}{Timer(self.timeAway)}  {cl.RED}]{cl.MAGENTA}[  {cl.CYAN}{Timer(curentTime.hour * 60 + curentTime.minute)}   {cl.MAGENTA}]{st.RESET_ALL}')
            self.apart = False
    
    def CrtlC(self):
        print(f'\r{cl.GREEN}[ {cl.CYAN}{Timer(self.logTime + self.timeCtrlC)} {cl.GREEN}]{cl.RED}[ {cl.CYAN}{Timer(0)}  {cl.RED}]{cl.MAGENTA}[  {cl.CYAN}{Timer(datetime.now().hour * 60 + datetime.now().minute)}   {cl.MAGENTA}]{st.RESET_ALL}')
        print(f"{cl.RED}exiting...{st.RESET_ALL}")