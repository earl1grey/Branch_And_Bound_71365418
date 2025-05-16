import tkinter as tk
from Resources.menu import Main_Menu

def run_app():
    root = tk.Tk()
    app = Main_Menu(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()