import os, shutil
from Quartz import CGSessionCopyCurrentDictionary as Session
from Timer import Timer
        
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

def removeCache():
    home = os.path.expanduser('~')
    os.chdir(home+'/.tools/plog')
    shutil.rmtree("__pycache__")

if __name__ == '__main__':
    lunch()
    removeCache()