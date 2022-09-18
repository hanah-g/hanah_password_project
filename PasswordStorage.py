import hashlib
import re
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

#instead of manual, use someone else's

#master = input("What is your master password?")

#salt = os.urandom(16)
#kdf = PBKDF2HMAC(
    #algorithm=hashes.SHA256(),
    #length=32,
    #salt=salt,
    #iterations=390000,
#)
#key = base64.urlsafe_b64encode(kdf.derive(master.encode()))
#f = Fernet(key)

#then store key in master.key

file = open("master.key", "rb")
key = file.read()
file.close()

f = Fernet(key)

def strengthTest():
    password = input("Please enter your password: ")
    if len(password) > 7:
        if bool(re.match('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]))', password)) == True:
            # checking if it contains at least one of each category
            print("The password is strong.")

            # since it is valid, check if it is one of 100 most used!

            # pws aren't cleartext, need to encode in utf-8
            encoded_pw = password.encode("utf-8")
            pw_hash = hashlib.md5(encoded_pw.strip()).hexdigest()
            # using hashlib here. strip is to remove extraneous chars. this gives us the hash to compare!

            passlist = open(os.path.expanduser("~/Desktop/top100pws.txt"))
            # we want to read the list now for our loop!

            for word in passlist:
                encoded_word = word.encode("utf-8")
                word_hash = hashlib.md5(encoded_word.strip()).hexdigest()
                # going through the list and making the hashes

                if word_hash == pw_hash:
                    print("This is a commonly used password. The password was " + word + ".")
                    quit()

            print("Your supplied password is not one of the 100 most used passwords!")

        else:
            print("Your password is too short and/or does not contain nums, uppers, lowers, AND special chars.")

def addNewAccount():
    # This function will append new password in the txt file
    acc = input("Please enter what this is an account for: ")
    usr = input("Enter the email or user associated with the account: ")
    pwd = input("Please enter the password associated with the account: ")

    with open('manager.txt', 'a') as manager:
        #creates the file if it doesn't exist with "a" mode
        manager.write(acc + "|" + usr + "|" + f.encrypt(pwd.encode()).decode() + "\n")
        #writes account, username, and encrypted password

def viewManager():
    accFind = input("What account are you looking for?")
    with open('manager.txt', 'r') as manager:
        for line in manager.readlines():
            accountInfo = line.rstrip()
            #get rid of return after the lines
            acc, usr, pwd = accountInfo.split("|")
            #separates each with the | inserted earlier -> solution for mutliple words
            if (accFind == acc):
                print("Account:", acc, "| User:", usr, "| Password:",
                f.decrypt(pwd.encode()).decode())
#refactoring of original code. encrypts rather than cleartext, much safer
#r mode = can only read this file


