from Quartz import CGSessionCopyCurrentDictionary as Session
from Timer import Timer
from Update import *
from colorama import Fore as cl
from colorama import Style as st

def lunch():
    alive = True
    calcul = Timer()
    calcul.printHead()
    while alive:
        try:
            dic = Session()
            state = 'kCGSSessionOnConsoleKey' in dic.keys() or dic['kCGSSessionOnConsoleKey'] == False
            state = (state == True) and (('CGSSessionScreenIsLocked' in dic.keys() and dic['CGSSessionScreenIsLocked'] == True))
            if state == True:
                calcul.screenLocked()
            else:
                calcul.logedBack()
        except KeyboardInterrupt:
            calcul.CrtlC()
            alive = False
            return 0

if __name__ == '__main__':
    if UpToDate() == True:
        print(f"There is an UpDate available do you wand to update ({cl.GREEN}Y{st.RESET_ALL}/{cl.RED}n{st.RESET_ALL}): ", end='')
        choice = input().lower()
        if choice == 'y' or choice == 'yes':
            UpDate()
    lunch()
    removeCache()
    