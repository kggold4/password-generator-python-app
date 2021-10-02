import tkinter as tk
from GUI import Gui

if __name__ == '__main__':
    root = tk.Tk()
    app = Gui(master=root)
    app.mainloop()
