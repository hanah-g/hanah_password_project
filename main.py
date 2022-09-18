from PasswordStorage import *

# PROCESS
# need a list of passwords to use, find online most common
# create and edit the text file with text editor, then make path to that file as the file to be used
# NOTE: can be changed with a more robust list (this is top 100 from wikipedia)

# check if password is strong
# check if password is on 100 most used
mode = input("Do you want to check a password (check), view passwords (view), or add a new one (add)? Use 'quit' to quit.")

while True:
    if mode == "quit":
        break
    if mode == "check":
        strengthTest()
        mode = input("What do you want to do next?")
    elif mode == "add":
        addNewAccount()
        mode = input("What do you want to do next?")
    elif mode == "view":
        viewManager()
        mode = input("What do you want to do next?")
    else:
        print("Invalid input. Please try again.")
        break
