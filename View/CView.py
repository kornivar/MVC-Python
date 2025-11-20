import tkinter as tk


class CView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("300x275")
        self.root.title("Calculator")
        self.root.configure(bg="lightblue")
        self.init_interfase()

    def init_interfase(self):
        self.entry_a = tk.Entry(self.root, width=15)
        self.entry_b = tk.Entry(self.root, width=15)

        self.entry_a.grid(row=0, column=2, padx=(70, 0), pady=10)
        self.entry_b.grid(row=1, column=2, padx=(70, 0), pady=10)

        btn_add = tk.Button(self.root, text="+", width=5, command=self.controller.add)
        btn_sub = tk.Button(self.root, text="-", width=5, command=self.controller.subtract)
        btn_mul = tk.Button(self.root, text="*", width=5, command=self.controller.multiply)
        btn_div = tk.Button(self.root, text="/", width=5, command=self.controller.divide)

        btn_add.grid(row=0, column=0, padx=5, pady=10)
        btn_sub.grid(row=0, column=1, padx=5, pady=10)
        btn_mul.grid(row=1, column=0, padx=5, pady=10)
        btn_div.grid(row=1, column=1, padx=5, pady=10)

        self.label_result = tk.Label(self.root, text="", fg="blue")
        self.label_result.grid(row=4, column=0, columnspan=3, pady=10, padx=(40, 40))

    def get_numbers(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            return a, b
        except ValueError:
            raise ValueError("Error: Invalid input. Please enter numeric values.")

    def display_result(self, result):
        self.label_result.config(text=f"{result}")

    def start(self):
        self.root.mainloop()