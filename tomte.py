#Abion Paulsson, Elliot Eriksson
#TEINF-20
#2021-12-15
#Önskelist Skapare

#imports neccesary features
import time
import os
import random

#clears the console
def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#makes a new list
def new():
    clearconsole()
    filename = input("Please input file name: ")
    filename = filename + ".txt"
    with open(f"Python/Substitute-Santa/{filename}","w", encoding="utf8") as f:
        recievername = input("Please Input name of reciever: ")
        f.write(f"-List of {recievername}-\n")
        while True:
            present = input("Please name something you would like to add to the wish list, or quit: ")
            if present == "quit":
                break
            else:
                f.write(f"{present}\n")

#reads a existing list
def read():
    clearconsole()
    filename = input("Please input file name: ")
    filename = filename + ".txt"
    with open(f"Python/Substitute-Santa/{filename}", "r", encoding="utf8") as f:
        for line in f.readlines():
            print(line)
        input("Press enter to return ")

#reads the naughty list, and then gives you the option to add names to it
def naughty():
    clearconsole()
    with open(f"Python/Substitute-Santa/kolbarn.txt", "r", encoding="utf8") as f:
        #Code courtesy of Elliot
        naughtylist=f.read().splitlines()
    
    print(f"Names already on the Naughty List: {naughtylist}\n")
    
    with open(f"Python/Substitute-Santa/kolbarn.txt", "a", encoding="utf8") as f:
        while True:
            name= input("Input a name to add to the naughty list, or quit: ")
            if name == "quit":
                break
            else:
                f.write(f"{name}\n")

#reads the naughty list and prints the names
def naughtyread():
    clearconsole()
    print("Names on the Naughty list:\n")
    with open(f"Python/Substitute-Santa/kolbarn.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            print(line)
        input("Press enter to return. ")

#main function
def start():
    clearconsole()
    load = ("Initializing")
    for i in range(4):
        print(load)
        load += "."
        time.sleep(1)
        clearconsole()
    while True:
        clearconsole()
        menuchoice = input("""
| WishList9000.exe
|
| >New List
|
| >Read List
|
| >Naughty List
|
| >Read Naughty List
|
| >Quit
|
| © Santa Inc, 1987
|
| Choose Option [New/Read/Naughty/Naughtyread/Quit]: """)

        if menuchoice.capitalize() == "New":
            new()
        elif menuchoice.capitalize() == "Read":
            read()
        elif menuchoice.capitalize() == "Naughty":
            naughty()
        elif menuchoice.capitalize() == "Naughtyread":
            naughtyread()
        elif menuchoice.capitalize() == "Quit":
            os._exit()

start()