def main():
    while True:
        try:
            res = eval(input(">: "))
            print(res)
        except (ValueError, TypeError, NameError, SyntaxError) as e:
            print(f"Err: {e}")
main()