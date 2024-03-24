import os, shutil, sys, time, subprocess
from Quartz import CGSessionCopyCurrentDictionary as Session
from Timer import Timer
from subprocess import Popen, PIPE
from colorama import Fore as cl
from colorama import Style as st

# Printing the the loading message
def print_load():
    sys.stdout.write(f'\rUpdating:[{cl.GREEN}--{st.RESET_ALL}] ')
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\rUpdating:[{cl.GREEN}\\{st.RESET_ALL}] ')
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\rUpdating:[{cl.GREEN}|{st.RESET_ALL}] ')
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\rUpdating:[{cl.GREEN}/{st.RESET_ALL}] ')
    sys.stdout.flush()
    time.sleep(0.2)

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

"""
This function checks if the local branch is up to date with the remote branch.

Returns:
    True if the local branch is up to date, False otherwise.
"""
def UpToDate():
  # Use subprocess to run git commands
  try:
     # Fetch latest information from the remote branch
    fetch_process = Popen(['git', 'fetch'], stdout=PIPE, stderr=PIPE)
    fetch_process.wait()  # Wait for fetch to complete

    # Check the status of the local branch
    status_process = Popen(['git', 'status', '-uno'], stdout=PIPE, stderr=PIPE)
    status_output, status_err = status_process.communicate()  # Obtain output and error
    status_process.wait()

    if status_err:
      raise RuntimeError(f"Error checking branch status: {status_err.decode()}")

    # Check for "your branch is up to date" message
    return "your branch is up to date" in status_output.decode()

  except Exception as e:
    # Print a more informative error message
    print(f"An error occurred while checking branch status: {e}")
    return False

def UpDate():
    os.chdir('/Users/faksouss/.tools/cclass')
    Updating = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
    while Updating.poll() is None:
        print_load()
    sys.stdout.write(f'\rUpdating:{cl.GREEN}✓{st.RESET_ALL} ')
    sys.stdout.flush()
    print()
    ExtSts = Updating.wait()
    if ExtSts != 0:print(f"{cl.RED}ERROR :{st.RESET_ALL}Updating failed.", file=sys.stderr)
    else:print(f"{cl.GREEN}SUCSSES : {st.RESET_ALL}Command updated sucssesfully.")

def removeCache():
    home = os.path.expanduser('~')
    os.chdir(home+'/.tools/plog')
    shutil.rmtree("__pycache__")

if __name__ == '__main__':
    if UpToDate() == True:
        print(f"There is an UpDate available do you wand to update ({cl.GREEN}Y{st.RESET_ALL}/{cl.RED}n{st.RESET_ALL}): ", end='')
        choice = input().lower()
        if choice == 'y' or choice == 'yes':
            UpDate()
    
    lunch()
    removeCache()
    