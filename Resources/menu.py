import tkinter as tk
from tkinter import messagebox

class Main_Menu:
    def not_exist(self):
        print("Функция не существует")
        
    def __init__(self, root):
        self.launcher = root
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
        self.create_matrix_button.config(command=self.draw_matrix_grid, font=("Arial", 14, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
        self.create_matrix_button.pack(padx=50, pady=20) # Заполнение и отступ

        self.back_button = tk.Button(self.matrix_menu, text="Назад") # Кнопка для возвращения в меню
        self.back_button.config(command=self.back_to_menu, font=("Arial", 14, 'bold'), bg='#0a1e80', fg='#ffffff', activebackground='#deebff') # Параметры создания
        self.back_button.pack(padx=50, pady=20) # Заполнение и отступ

        self.matrix_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Центрирование

    def back_to_menu(self):
        self.matrix_menu.pack_forget() # Сокрытие меню матрицы
        self.main_menu.pack(fill='both', expand=True) # Вызов главного меню

    def draw_matrix_grid(self):
        try:
            size = int(self.matrix_size_enter.get()) # Приёмка введённого значения

            if size > 24: # Проверка максимального значения
                messagebox.showerror("Произошла ошибка", "Максимальный размер матрицы должен быть не больше 24!") # Вывод сообщения
                return

            self.matrix_menu.place_forget() # Очистка экрана от кнопок

            self.matrix_setup = tk.Frame(self.primaryscreen, bg='#ccd4f0', padx=10, pady=10) # Создание новой рабочей области
            self.matrix_setup.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Центрирование

            self.elements = [] # Список элементов матрицы

            for i in range(size):
                temp = [] # Временное хранилище для элементов матрицы, до переноса в elements
                for j in range(size): # Цикл для определения размера матрицы и генерации её
                    if i == j:
                        element = tk.Entry(self.matrix_setup, width=5, justify='center', font=('Arial', 14)) # Ввод элемента, если i = j
                        element.insert(0, "∞") # Вставка ∞ на место равнения
                        element.config(state='disabled') # Отключение ввода для клеток i = j
                        temp.append(element) # Запоминание элементов
                    else:
                        element = tk.Entry(self.matrix_setup, width=5, justify='center', font=('Arial', 14)) # Создание ввода для остальных элементов
                        temp.append(element) # Запоминание клеток с взаимодействием
                    element.grid(row=i, column=j, padx=1, pady=1) # Помещение элементов в условную сетку
                self.elements.append(temp) # Глобальная память элементов матрицы

            self.start = tk.Button(self.matrix_setup, text="Решить", font=('Arial', 14, 'bold'), bg='#d4173d', fg='#ffffff', activebackground='#f5a24e') # Создание кнопки решения
            self.start.config(command=self.not_exist) # Параметры кнопки
            self.start.grid(row=size, columnspan=size, pady=10) # Настройка отображения в условной сетке

            self.back_matrix = tk.Button(self.matrix_setup, text="Назад") # Кнопка для возвращения в меню
            self.back_matrix.config(command=self.back, font=("Arial", 14, 'bold'), bg='#0a1e80', fg='#ffffff', activebackground='#deebff') # Параметры создания
            self.back_matrix.grid(row=size+1, columnspan=size, padx=50, pady=20) # Заполнение и отступ

        except ValueError: # Ошибка при неправильном значении
            messagebox.showerror("Произошла ошибка", "Введите корректный размер матрицы!") # Вызов сообщения с ошибкой         
    
    def back(self):
        self.matrix_setup.place_forget() # Сокрытие меню решения
        self.main_menu.pack(fill='both', expand=True) # Вызов главного меню

if __name__ == "__main__": # Условие запуска
    root = tk.Tk()
    app = Main_Menu(root)
    root.mainloop()