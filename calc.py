import ast
def main():
    while True:
        try:
            res = float(ast.literal_eval(input(">: ")))
            print(res)
        except (ValueError, TypeError, NameError, SyntaxError, KeyboardInterrupt) as e:
            print(f"Err: {e}")
main()