import ast
def main():
    while True:
        try:
            res = float(ast.literal_eval(input(">: ")))
            print(res)
        except (ValueError, TypeError, NameError, SyntaxError) as e:
            print(f"Err: {e}")
main()