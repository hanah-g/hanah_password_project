import os.path

def getManager():
    if os.path.exists("manager.txt"):
        pass
    else:
        file = open("manager.txt", 'w')
        #makes a file if one does not already exist w/ 'w'
        file.close()


def addNewAccount():
    # This function will append new password in the txt file
    file = open("manager.txt", 'a')

    acc = input("Please enter what this is an account for: ")
    usr = input("Enter the email or user associated with the account: ")
    pwd = input("Please enter the password associated with the account: ")

    print()
    print()

    acc2 = "Account: " + acc + "\n"
    usr2 = "UserName: " + usr + "\n"
    pwd2 = "UserName: " + pwd + "\n"

    file.write("---------------\n")
    file.write(acc2)
    file.write(usr2)
    file.write(pwd2)
    file.write("---------------\n")
    file.write("\n")
    file.close()

def printManager():
    file = open('manager.txt', 'r')
    content = file.read()
    file.close()
    print(content)





