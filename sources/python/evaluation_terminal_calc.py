import time
import os
import sys
def start():
    dashes2 = "-------------------------------------"
    os.system('cls||clear')
    print(dashes2)
    print(f"Welcome to the evaluation calculator!\n{dashes2}")
    print("1. Start\n2. Instructions")
    try:
        op = int(input(">: "))
        if op == 1:
            main()
        elif op == 2:
            os.system('cls||clear')
            print(dashes)
            print(f"Instructions\n{dashes}\n>: 23-4-2\n17")
            for remaining in range(5, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Instructions clear in {:2d}".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            start()
    except ValueError as e:
        print(f"Err: {e}")
def define():
    global dashes
    dashes = "------------------------"
    start()
def main():
    os.system('cls||clear')
    print(dashes)
    print(f'Evaluation Calculator\n{dashes}\nType "exit()" to exit the program\n')
    while True:
        try:
            res = eval(input(">: "))
            print(res, "\n")
        except (SyntaxError, NameError, TypeError, ValueError) as e:
            print(f"Err: {e}")
define()
