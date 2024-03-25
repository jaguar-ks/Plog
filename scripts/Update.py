import sys, subprocess, os, time, shutil
from subprocess import Popen, PIPE
from colorama import Fore as cl
from colorama import Style as st

###################################
# Printing the the loading message
###################################
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

###################################################################
# Checks if the local branch is up to date with the remote branch.
# 
# Returns:
#     bool: True if the branch is up to date, False otherwise.
###################################################################
def UpToDate():
    # Going to script Path
    home = os.path.expanduser('~')
    os.chdir(home + '/.tools/plog')
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

###################################################################################
# Updates the command by pulling the latest changes from the git repository.
# 
# This function changes the current working directory to the script path,
# performs a git pull to fetch the latest changes, and waits for the process
# to finish. If the update is successful, it prints a success message. Otherwise,
# it prints an error message.
# 
# Note: This function assumes that the git command is available in the system.
# 
# Returns:
#     None
###################################################################################
def UpDate():
    # Going to script Path
    home = os.path.expanduser('~')
    os.chdir(home + '/.tools/plog')
    Updating = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
    # Waiting  for the process to finish and printing a loading message
    while Updating.poll() is None:
        print_load()
    sys.stdout.write(f'\rUpdating:{cl.GREEN}✓{st.RESET_ALL} ')
    sys.stdout.flush()
    print()
    ExtSts = Updating.wait()
    # Checking if the update is done successfully and printing a message accordingly
    if ExtSts != 0:
        print(f"{cl.RED}ERROR :{st.RESET_ALL}Updating failed.", file=sys.stderr)
    else:
        print(f"{cl.GREEN}SUCCESS : {st.RESET_ALL}Command updated successfully.")

###################################################################################
# Removes the cache directory "__pycache__" in the script path.
# 
# This function changes the current working directory to the script path and then 
# deletes the cache directory "__pycache__" using the `shutil.rmtree` function.
# 
# Note: This function assumes that the cache directory exists in the script path.
###################################################################################
def removeCache():
    # Going to the script path
    home = os.path.expanduser('~')
    os.chdir(home+'/.tools/plog/scripts')
    # Deleting the cache directory
    shutil.rmtree("__pycache__")
