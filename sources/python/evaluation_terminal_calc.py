def define():
    global dashes
    dashes = "------------------------"
    main()
def main():
    print(dashes)
    print(f'Evaluation Calculator\n{dashes}\nType "exit()" to exit the program\n')
    while True:
        try:
            res = eval(input(">: "))
            print(res, "\n")
        except (SyntaxError, NameError, TypeError, ValueError) as e:
            print(f"Err: {e}")
define()
