from PasswordStorage import *
import hashlib
import re
import os

#PROCESS
#need a list of passwords to use, find online most common
#create and edit the text file with text editor, then make path to that file as the file to be used
# NOTE: can be changed with a more robust list (this is top 100 from wikipedia)

#check if password is strong
#check if password is on 100 most used

toDo = input("Do you want to check a password? Enter 'yes' if so.")
if toDo == "yes":
    password = input("Please enter your password: ")
    if len(password)>7:
        if bool(re.match('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]))',password)) == True:
            #checking if it contains at least one of each category
            print("The password is strong.")

            #since it is valid, check if it is one of 100 most used!

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

else:
    #go to password storage
    getManager()
    addNew = input("Do you want to add a new password? Enter 'yes' if so.")
    if (toDo == "yes"):
        addNewAccount()
    printManager()








