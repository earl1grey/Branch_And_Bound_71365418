import tkinter as tk

def not_exist():
    print("Функция не существует")

launcher = tk.Tk() #создание меню

launcher.title("Задача коммивояжера")
launcher.geometry = ("800x800")


solver = tk.Button(launcher, text="Начать решение")
solver.config(command=not_exist, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff')
solver.pack(fill="both", expand=True) #расположение первой кнопки

history = tk.Button(launcher, text="История решений")
history.config(command=not_exist, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff')
history.pack(fill="both", expand=True) #расположение второй кнопки

prog_exit = tk.Button(launcher, text="Выход")
prog_exit.config(command=launcher.quit, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff')
prog_exit.pack(fill="both", expand=True) #расположение третьей кнопки

launcher.mainloop() #цикл программы