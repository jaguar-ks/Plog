import os

from Quartz import CGSessionCopyCurrentDictionary as Session

from datetime import datetime

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
    Hours = 0
    Minutes = 0
    
    def __init__(self, M=0):
        self.Hours = M // 60
        self.Minutes = M % 60
    
    def __str__(self):
        Tm = str(self.Hours)
        if len(Tm) == 1:Tm = '0'+Tm
        Mn = str(self.Minutes)
        if len(Mn) == 1:Mn = '0'+Mn
        return Tm + ':' + Mn

def lunch():
    start = lock = datetime.now()
    logTime = timeAway = 0
    alive = apart = True
    print(f'\t[StartTime {start.strftime("%H:%M")}]')
    print(f"[LogTime]|[TimeAway]|[CurentTime]")
    while alive:
        try:
            dic = Session()
            state = 'kCGSSessionOnConsoleKey' in dic.keys() or dic['kCGSSessionOnConsoleKey'] == False
            state = (state == True) and (('CGSSessionScreenIsLocked' in dic.keys() and dic['CGSSessionScreenIsLocked'] == True))
            if state == True:
                if apart == False:
                    lock = datetime.now()
                    logTime += ((lock.hour - start.hour) * 60) + (lock.minute - start.minute) 
                    start = datetime.now()
                    apart = True
            else:
                if apart == True:
                    curentTime = datetime.now()
                    timeAway = curentTime.minute - lock.minute
                    print(f'[ {Timer(logTime)} ]|[ {Timer(timeAway)}  ]|[  {curentTime.strftime("%H:%M")}   ]')
                    apart = False
        except KeyboardInterrupt:
            alive = False
            curentTime = datetime.now()
            timeAway = curentTime.minute - lock.minute
            print(f'[ {Timer(logTime)} ]|[ {Timer(timeAway)}  ]|[  {curentTime.strftime("%H:%M")}   ]')
            apart = False
            print('\rexiting...')

if __name__ == '__main__':
    lunch()