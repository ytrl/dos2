#gonna put it all in a single file for faster response

import os
import sys
import random
from time import sleep

dbfper = 0
unlock = 0
pswdatmtnum = 0
passfile1 = open("passfile.ytr","r")
passfile = passfile1.read()
username1 = open("username.ytr","r")
username = username1.read()

while dbfper <= 100:
	print("Loading Database Files: {dbfper}%".format(dbfper=dbfper))
	sys.stdout.write("\033[F") # Cursor up one line
	dbfper = dbfper + 6.25
	sleep(random.uniform(0.1, 0.2))

intper = 0

print("")

while intper <= 100:
	print("Loading Initialisation Data: {intper}%".format(intper=intper))
	sys.stdout.write("\033[F") # Cursor up one line
	intper = intper + 6.25
	sleep(random.uniform(0.1, 0.2))


print("")
print(" __  ____  _") ; sleep(0.2)
print("/     |    |") ; sleep(0.2)
print("\     |    |") ; sleep(0.2)
print(" --   |    -") ; sleep(0.2)
print("") ; sleep(0.2)
print("© Carrot Tech Industries") ; sleep(0.2)
print("A sub division of Yetroll®") ; sleep(0.2)
print("Loading cOS 1.3.1...") ; sleep(2)
print("---------------------")
print("User:", username)
while unlock == 0:
    if passfile == "null":
        input("Press Enter")
        unlock = 1
    else:
        if pswdatmtnum <=5:
            pswdatmt = input("Enter Password")
            if pswdatmt == passfile:
                unlock = 1
            else:
                unlock = 0
                pswdatmtnum = pswdatmtnum + 1
                print(pswdatmtnum, "Attempts")
        else:
            exit()
sysRun = 0
while sysRun == 0:
    commandInput = input("main.py     ")
    if commandInput == "/help":
        print("Use /sysinfo to bring up information about the system!")
    else:
        if commandInput == "/calculator":
            try:
                n = 0
                k = 0
                operation = 0
                while n == 0:
                    k = 0
                    operation = 0
                    print("darrotOS calculator by Daniel071")
                    input("Press enter to continue!")
                    while operation == 0:
                        print("Would you like for me to")
                        print("Add (a)")
                        print("Subtract (s)")
                        print("Multiply (m)")
                        inputAnswer = input("or Divide? (d)")
                        if inputAnswer == "a":
                            operation = "a"
                        else:
                            if inputAnswer == "s":
                                operation = "s"
                            else:
                                if inputAnswer == "m":
                                    operation = "m"
                                else:
                                    if inputAnswer == "d":
                                        operation = "d"
                                    else:
                                        print("Sorry! Please use either a, s, m or d")
                    firstNumber = int(input("What is your first number? "))
                    secondNumber = int(input("What is your second number? "))
                    if inputAnswer == "a":
                        answer = firstNumber + secondNumber
                    else:
                        if inputAnswer == "s":
                            answer = firstNumber - secondNumber
                        else:
                            if inputAnswer == "m":
                                answer = firstNumber * secondNumber
                            else:
                                if inputAnswer == "d":
                                    answer = firstNumber / secondNumber
                    print("Your answer was", answer)
                    while k == 0:
                        inputAnswer = input("New calculation? [y / n] ")
                        if inputAnswer == "n":
                            n = 1
                            k = 1
                        else:
                            if inputAnswer == "y":
                                print("Repeating")
                                k = 1
                            else:
                                print("Please enter either [y / n]")
            except:
                print("err_calc_crash. Please try again.")
