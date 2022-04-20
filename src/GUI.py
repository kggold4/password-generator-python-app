import tkinter as tk
from Password import generate_random_password
from Constants import Design as const


class Gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.title = tk.Text(self, font=const.FONT_FAMILY, bg=const.LIGHT_GREY, height=1, width=30)
        self.input_len = tk.Entry(self, justify=tk.CENTER, font=const.FONT_FAMILY)
        self.generate_btn = tk.Button(
            self, font=const.FONT_FAMILY, text="Generate", command=self.generate, cursor=const.CURSOR)
        self.output_password = tk.Text(self, font=const.FONT_FAMILY, height=1, width=30)
        self.quit = tk.Button(
            self, font=const.FONT_FAMILY, text="QUIT", fg=const.RED, command=self.master.destroy, cursor=const.CURSOR)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title.pack()
        self.input_len.pack()
        self.generate_btn.pack()
        self.output_password.pack()
        self.quit.pack()
        self.title.insert(tk.END, const.TITLE)
        self.input_len.focus_set()

    def generate(self):
        self.output_password.delete('1.0', tk.END)
        length = int(self.input_len.get())
        if length == '' or length is None:
            return
        self.output_password.insert(tk.END, generate_random_password(length))
