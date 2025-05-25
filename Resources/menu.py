import tkinter as tk
from tkinter import messagebox
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from .desicion_logic import Logic

class Main_Menu:       
    def __init__(self, root):
        self.launcher = root # Приложению присваивается значение root
        self.launcher.title("Задача коммивояжера") # Окну присваивается название
        self.launcher.geometry("800x800") # Параметры окна
        self.result = [] # Хранилище результата выполненного запроса
        self.history = [] # Хранилище для показа всех результатов
        
        self.primaryscreen = tk.Frame(self.launcher) # Cоздаётся вспомогательная область для удобного переключения между окнами
        self.primaryscreen.pack(fill='both', expand=True) # Заполнение области программы
        
        self.main_menu = tk.Frame(self.primaryscreen) # Создание области для меню программы

        for widget in self.main_menu.winfo_children(): # Очистка элементов
            widget.destroy()

        solver = tk.Button(self.main_menu, text="Начать решение") # Создание кнопки "Начать решение"
        solver.config(command=self.matrix_creator, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
        solver.pack(fill="both", expand=True, padx=50, pady=20) # Заполнение и отступ

        history = tk.Button(self.main_menu, text="История решений") # Создание кнопки "История решений"
        history.config(command=self.save_history, font=("Arial", 20, 'bold'), bg='#aeccfc', activebackground='#deebff') # Параметры создания
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
        self.matrix_menu.place_forget() # Сокрытие меню матрицы
        self.main_menu.pack(fill='both', expand=True) # Вызов главного меню

    def draw_matrix_grid(self):
        try:
            size = int(self.matrix_size_enter.get()) # Приёмка введённого значения

            if size < 2: # Проверка минимального значения
                messagebox.showerror("Произошла ошибка", "Минимальный размер матрицы должен быть не меньше 2!") # Вывод сообщения
                return

            if size > 5: # Проверка максимального значения
                messagebox.showerror("Произошла ошибка", "Максимальный размер матрицы должен быть не больше 5!") # Вывод сообщения
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
                        element.insert(0, "∞") # Вставка ∞ на место равнения городов
                        element.config(state='disabled') # Отключение ввода для клеток i = j
                        temp.append(element) # Запоминание элементов
                    else:
                        element = tk.Entry(self.matrix_setup, width=5, justify='center', font=('Arial', 14)) # Создание ввода для остальных элементов
                        temp.append(element) # Запоминание клеток с взаимодействием
                    element.grid(row=i, column=j, padx=1, pady=1) # Помещение элементов в условную сетку
                self.elements.append(temp) # Глобальная память элементов матрицы

            self.start = tk.Button(self.matrix_setup, text="Решить", font=('Arial', 14, 'bold'), bg='#d4173d', fg='#ffffff', activebackground='#f5a24e') # Создание кнопки решения
            self.start.config(command=self.matrix_entry) # Параметры кнопки
            self.start.grid(row=size, columnspan=size, pady=10) # Настройка отображения в условной сетке

            self.back_matrix = tk.Button(self.matrix_setup, text="Назад") # Кнопка для возвращения в меню
            self.back_matrix.config(command=self.back, font=("Arial", 14, 'bold'), bg='#0a1e80', fg='#ffffff', activebackground='#deebff') # Параметры создания
            self.back_matrix.grid(row=size+1, columnspan=size, padx=50, pady=20) # Заполнение и отступ

        except ValueError: # Ошибка при неправильном значении
            messagebox.showerror("Произошла ошибка", "Введите корректный размер матрицы!") # Вызов сообщения с ошибкой         
    
    def back(self): # Метод для окна с заполнением матрицы
        self.matrix_setup.place_forget() # Сокрытие меню решения
        self.main_menu.pack(fill='both', expand=True) # Вызов главного меню

    def matrix_entry(self): # Метод заполнения матрицы
            matrix_size = len(self.elements) # Считывание количества элементов матрицы
            matrix = np.zeros((matrix_size, matrix_size), dtype=float) # Возвращение массива, заполненного нулями
            
            try: # Заполнение
                for i in range(matrix_size):
                    for j in range(matrix_size):
                        if i != j:
                            cell = self.elements[i][j].get() # Получение чисел из ячеек
                            if cell == "∞":
                                matrix[i][j] = float('inf') # Присвоение нулевым ячейкам бесконечности
                            else:
                                if cell.strip() == "": # Проверка на пустое значение
                                    messagebox.showerror("Ошибка","Пустое значение в ячейке!") # Вывод ошибки
                                    return
                                matrix[i][j] = float(cell) # Преобразование значения и присвоение его к ячейке
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректное значение в ячейке!") # Вывод ошибки при написании символов вместо чисел
                return

            for i in range(matrix_size): # Проверка на нули и отрицательные числа
                for j in range(matrix_size):
                    if i != j:
                        cell = self.elements[i][j].get() # Получение чисел из ячеек
                        try:
                            cell_val = float(cell) # Присвоение значения ячейки
                            if cell_val <= 0: # Проверка
                                messagebox.showerror("Ошибка", f"Значение в ячейке ({i+1}, {j+1}) должно быть больше нуля") # Вывод ошибки
                                return
                        except ValueError: # Игнорировать ошибку значений
                            continue

            matrix_decision = Logic(matrix) # Присвоение matrix_decision класса Logic для избежания ошибки
            path, value = matrix_decision.solve() # Выполнение метода

            letter = [chr(65 + i) for i in path] # Преобразование числа в букву
            log = f"№{len(self.history) + 1}: {' -> '.join(letter)}; Стоимость: {int(value)}" # Маска результата для сохранения решений 
            self.history.append(log) # Запись сохранения

            messagebox.showinfo("Результат", f"Полный путь: {' -> '.join(letter)}; Стоимость: {int(value)}") # Показ результата
            
            self.matrix_visualization(matrix_decision.decision_tree, optimal_path=path) # Вывод дерева решений

    def matrix_visualization(self, decision_tree, optimal_path=None):
        try:
            fig, ax = plt.subplots(figsize=(16, 10)) # Задание размера объекту и расположение на оси, где figsize - кортеж ширины и высоты

            start = next((n for n in decision_tree.nodes if str(n) == "Начало"), None) # Нахождение начала решения
            if start is None: # Проверка на нахождение начала решения
                start = next(iter(decision_tree.nodes), None) # Назначение первого попавшегося узла началом решения, в том случае если начало решения не было найдено

            branches = [] # Список границ
            if optimal_path:
                path_str = [] # Список для преобразованного в строку пути
                for i in range(len(optimal_path)):
                    path_str.append(chr(65 + optimal_path[i])) # Добавление в список преобразованного в строку пути
                    if i > 0: # Проверка, что обрабатывается не первый элемент optimal_path
                        branch = " -> ".join(path_str[:i]) + " -> " + path_str[i] # Создание границ
                        branches.append(branch) # Внесение границ в список границ
            
            pos = {start: (0, 1)} # Размещение начала решения сверху по центру
            levels = {} # Создание словаря для группировки ветвей по уровням

            for node in decision_tree.nodes: # Группировка узлов по уровням 
                if node == start: # Проверка на начало решения
                    continue # Пропуск
                level = len(str(node).split(" -> ")) - 1 # Вычисление уровня узла
                levels.setdefault(level, []).append(node) # Группировка по уровню узла
            
            for level, nodes in levels.items(): # Распределение узлов на плоскости
                pos_y = 1.0 - level * 0.3 # Вертикальное позиционирование
                pos_x = np.linspace(-1, 1, len(nodes)) if len(nodes) > 1 else [0] # Распределение узлов друг от друга по горизонтали
                for node, x in zip(nodes, pos_x): # Объединение пунктов и их координат по горизонтали
                    pos[node] = (x, pos_y) # Присвоение координат для каждого узла
            
            lower_bounds = nx.get_node_attributes(decision_tree, 'lower_bound') # Получение нижних границ

            node_labels = {} # Словарь, который будет содержать текстовые подписи для каждого узла

            for node in decision_tree.nodes: # Рассмотрение каждого узла
                label_parts = [] # Для каждого узла создается список bound_text, который будет содержать подписи
                splitted_nodes = str(node).split(" -> ") # Разбиение узлов по разделителю
                if len(splitted_nodes) >= 2: # Если длина узла больше или равно 2 городам
                    path_part = f"{splitted_nodes[-2]}→{splitted_nodes[-1]}" # Направление из предпоследнего пункта в последний
                else:
                    path_part = str(node) # Иначе полное название узла
                label_parts.append(path_part) # Запись полученного названия узла в список
                if node in lower_bounds: # Проверка на наличие нижней границы
                    label_parts.append(f"H = {lower_bounds[node]}") # Запись нижней границы в список
                node_labels[node] = "\n".join(label_parts) # Объединение подписей

            dot_color = [] # Список для цветов узлов
            dot_size = [] # Список для размера узлов
            level_pairs = {} # Список для разделения узлов на подуровни
            
            for node in decision_tree.nodes:
                if node == start:
                    dot_color.append('#ad68f2')  # Присвоение точке начала решения фиолетового цвета
                    dot_size.append(2500) # Размер точки начала решения
                elif optimal_path and node in branches:
                    dot_color.append('#f06859')  # Присвоение точкам полного оптимального пути красного цвета
                    dot_size.append(2500) # Размер точки полного оптимального пути
                else:
                    dot_color.append('#75c5fa')  # Присвоение остальным точкам голубого цвета
                    dot_size.append(2000) # Размер остальных точек
                
                splitted_nodes = str(node).split(" -> ") # Разделение и включение в список пунктов
                level_pairs[node] = f"{splitted_nodes[-2]}→{splitted_nodes[-1]}" if len(splitted_nodes) >= 2 else str(node) # Преобразование в пару
            
            nx.draw_networkx_nodes(decision_tree, pos, node_color=dot_color, edgecolors='black', linewidths=1, node_size=dot_size, ax=ax) # Настройка отображения точек
            nx.draw_networkx_edges(decision_tree, pos, edge_color='#000000', width=2, arrows=True, arrowstyle='-|>', arrowsize=20, node_size=dot_size, ax=ax) # Настройка отображения границ
            nx.draw_networkx_labels(decision_tree, pos, labels=node_labels, font_size=10, font_weight='bold', ax=ax) # Отрисовка подписей
            
            ax.set_title("Дерево решений", fontsize=14) # Заголовок дерева решений
            ax.axis('off') # Отключение осей координат
            
            plt.tight_layout() # Оптимальное расположение для элементов, которые могут обрезаться
            plt.show() # Создание окна для отображения графа
            
        except Exception:
            messagebox.showerror("Ошибка", "Ошибка визуализации!") # Ошибка при неправильных данных визуализации
            return None

    def save_history(self):
            if not self.history: # Проверка на пустоту истории решений
                messagebox.showinfo("История решений", "История пуста.") # Сообщение
                return
            
            save_history_window = tk.Toplevel(self.launcher)  # Создание окна истории решений
            save_history_window.title("История решений") # Название окна
            save_history_window.geometry("800x800")  # Параметр размера окна
            
            save_history_title = tk.Label(save_history_window, text="История решений", font=("Arial", 18, 'bold')) # Заголовок
            save_history_title.pack(pady=10) # Отображение в окне
            
            results_list = tk.Listbox(save_history_window, font=("Arial", 14), width=40, height=15)  # Список решений
            results_list.pack(padx=20, pady=10) # Отображение в окне
            
            for result in self.history: # Поиск результатов в истории решений
                results_list.insert(tk.END, result) # Добавление результатов решений в список результатов
            
            close_button = tk.Button(save_history_window, text="Закрыть", command=save_history_window.destroy, font=("Arial", 14)) # Кнопка закрытия
            close_button.pack(pady=10) # Отображение в окне
