import tkinter as tk

class Main_Menu:
    def not_exist(self):
        print("Функция не существует")
        
    def __init__(self, launcher):
        self.launcher = launcher
        self.launcher.title("Задача коммивояжера") 
        self.launcher.geometry("800x800") # Параметры окна
        
        self.primaryscreen = tk.Frame(self.launcher) # Cоздаётся вспомогательная область для удобного переключения между окнами
        self.primaryscreen.pack(fill='both', expand=True) # Заполнение области программы
        
        self.main_menu = tk.Frame(self.primaryscreen) # Создание области для меню программы

        for widget in self.main_menu.winfo_children(): # Очистка элементов
            widget.destroy()

        solver = tk.Button(self.main_menu, text="Начать решение") # Создание кнопки "Начать решение"
        solver.config(command=self.matrix_creator, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
        solver.pack(fill="both", expand=True, padx=50, pady=20) # Заполнение и отступ

        history = tk.Button(self.main_menu, text="История решений") # Создание кнопки "История решений"
        history.config(command=self.not_exist, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
        history.pack(fill="both", expand=True, padx=50, pady=20) # Заполнение и отступ

        prog_exit = tk.Button(self.main_menu, text="Выход") # Создание кнопки "Выход"
        prog_exit.config(command=self.launcher.quit, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
        prog_exit.pack(fill="both", expand=True, padx=50, pady=20) # Заполнение и отступ

        self.main_menu.pack(fill='both', expand=True) # Заполнение области меню

        self.matrix_menu = tk.Frame(self.primaryscreen) # Создание области для меню матрицы

    def matrix_creator(self):
        for widget in self.matrix_menu.winfo_children(): # Очистка элементов
            widget.destroy()

        self.main_menu.pack_forget() # Для сокрытия главного меню в окне программы

        self.label_title = tk.Label(self.matrix_menu, text="Напишите размер матрицы:", font=("Arial", 16, 'bold')) # Создание текста
        self.label_title.pack(padx=50, pady=20) # Заполнение и отступ

        self.matrix_size_enter = tk.Entry(self.matrix_menu, font=("Arial", 16)) # Создание строки ввода
        self.matrix_size_enter.pack() # Отображение

        self.create_matrix_button = tk.Button(self.matrix_menu, text="Создать матрицу") # Кнопка для создания матрицы
        self.create_matrix_button.config(command=self.not_exist, font=("Arial", 14, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
        self.create_matrix_button.pack(padx=50, pady=20) # Заполнение и отступ

        self.back_button = tk.Button(self.matrix_menu, text="Назад") # Кнопка для возвращения в меню
        self.back_button.config(command=self.back_to_menu, font=("Arial", 14, 'bold'), bg='#0a1e80', fg='#ffffff', activebackground='#deebff') # Параметры создания
        self.back_button.pack(padx=50, pady=20) # Заполнение и отступ

        self.matrix_menu.pack(fill='both', expand=True) # Заполнение области меню

    def back_to_menu(self):
        self.matrix_menu.pack_forget() # Сокрытие меню матрицы
        self.main_menu.pack(fill='both', expand=True) # Вызов главного меню

if __name__ == "__main__": # Условие запуска
    root = tk.Tk()
    app = Main_Menu(root)
    root.mainloop()