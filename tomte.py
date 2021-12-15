import time
import os
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def new():
    filename = input("Please input file name: ")
    filename = filename + ".txt"
    with open(filename,"w", encoding="utf8") as f:
        recievername = input("Please Input name of reciever: ")
        f.write(f"-List of {recievername}-\n")
        while True:
            present = input("Please name something you would like to add to the wish list, or quit: ")
            if present == "quit":
                break
            else:
                f.write(f"{present}\n")

def read():
    filename = input("Please input file name: ")
    filename = filename + ".txt"
    with open(f"{filename}", "r", encoding="utf8") as f:
    # f.read läser hela filen
    # f.readlines ger en lista med alla rader som element
    # f.readline ger en rad i taget
        for line in f.readlines():
            print(line)

def start():
    load = ("Initializing")
    for i in range(4):
        print(load)
        load += "."
        time.sleep(1)
        clearConsole()
    while True:
        menuchoice = input("""
| WishList9000.exe
|
| >New List
|
| >Read List
|
| ©Santa Inc, 1987
|
| Choose Option [New/Read/Quit]: """)

        if menuchoice.capitalize() == "New":
            new()
        elif menuchoice.capitalize() == "Read":
            read()
        elif menuchoice.capitalize() == "Quit":
            os._exit()

start()