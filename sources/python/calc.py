def windowed_calculator():
    import tkinter as tk
    from tkinter import ttk
    import math

    class TI84Calculator:
        def __init__(self, root):
            self.root = root
            self.root.title("Windowed Calculator")
            
            self.entry = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief="solid")
            self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

            self.buttons = [
                ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
                ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
                ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
                ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
                ('sqrt', 5, 0), ('^', 5, 1), ('cos', 5, 2), ('sin', 5, 3),
                ('tan', 6, 0), ('log', 6, 1), ('exp', 6, 2), ('(', 6, 3),
                (')', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('C', 7, 3)
            ]

            self.create_buttons()

        def create_buttons(self):
            for (text, row, column) in self.buttons:
                if text == "=":
                    btn = ttk.Button(self.root, text=text, command=self.calculate)
                elif text == "C":
                    btn = ttk.Button(self.root, text=text, command=self.clear)
                else:
                    btn = ttk.Button(self.root, text=text, command=lambda t=text: self.button_click(t))
                btn.grid(row=row + 1, column=column, sticky="nsew", ipadx=10, ipady=10)

            for i in range(8):
                self.root.grid_rowconfigure(i, weight=1)
                self.root.grid_columnconfigure(i, weight=1)

        def button_click(self, text):
            current = self.entry.get()
            if text == 'pi':
                self.entry.insert(tk.END, str(math.pi))
            elif text == 'e':
                self.entry.insert(tk.END, str(math.e))
            else:
                self.entry.insert(tk.END, text)

        def clear(self):
            self.entry.delete(0, tk.END)

        def calculate(self):
            try:
                expression = self.entry.get()
                expression = expression.replace('^', '**')
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('log', 'math.log')
                expression = expression.replace('exp', 'math.exp')
                result = eval(expression, {"math": math})
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

    if __name__ == "__main__":
        root = tk.Tk()
        calculator = TI84Calculator(root)
        root.mainloop()

windowed_calculator()
