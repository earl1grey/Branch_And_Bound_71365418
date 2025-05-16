import numpy as np
import networkx as nx

class Logic:
    def __init__(self, matrix):
        self.matrix = matrix # Создаётся матрица

        self.matrix_lenght = len(matrix) # Присваивание длины матрицы

        self.optimal_path = None # Параметр оптимального пути
        self.optimal_value = float('inf') # Оптимальная стоимость, временно равная бесконечности
        self.decision_tree = nx.DiGraph() # Отображение графа

    def matrix_reduction(self, matrix):
        re_matrix = matrix.copy() # Создаётся копия исходной матрицы

        minimal_row = np.min(re_matrix, axis=1) # Возвращает минимум по горизонтали
        re_matrix = re_matrix - minimal_row[:, np.newaxis] # Преобразование всех минимальных элементов по строкам в столбец и вычитание из матрицы

        minimal_col = np.min(re_matrix, axis=0) # Возвращает минимум по вертикали
        re_matrix = re_matrix - minimal_col # Вычитание минимума по столбцам из матрицы

        return re_matrix, np.sum(minimal_row) + np.sum(minimal_col) # Возвращает преобразованную матрицу и нижнюю границу

    def choosing_path_value(self, path, value, re_matrix, previous_point):
        if len(path) == self.matrix_lenght: # Проверка на содержание всех городов в пути и завершение пути
            final_value = value + self.matrix[path[-1]][path[0]] # Полная стоимость с возвратом в начальный город
            if final_value < self.optimal_value: # Проверка на оптимальность (является ли этот путь лучше текущего)
                self.optimal_value = final_value # Обновление значения стоимости
                self.optimal_path = path # Обновление значения пути
                current_point = " -> ".join([chr(65 + x) for x in path]) # Объединение в узел
                self.decision_tree.nodes[current_point]['lower_bound'] = int(final_value) # Запись нижней границы для конечного узла
            return

        for i in range(self.matrix_lenght): # Перебор всех возможных городов
            if i not in path: # Проверка на посещение в текущем пути
                new_path = path + [i] # Создание нового пути с добавлением текущего города
                transit_value = self.matrix[path[-1]][i] # Стоимость перехода из последнего города в новый
                total_value = value + transit_value # Общая стоимость нового пути
                
                if total_value < self.optimal_value: # Если суммарная стоимость меньше оптимальной
                    new_re_matrix, re_value = self.matrix_reduction(re_matrix) # Редукция матрицы
                    total_lower_bound = total_value + re_value # Вычисление нижней границы для нового пути

                    current_point = " -> ".join([chr(65 + x) for x in new_path]) # Объединение в узел 
                    
                    if current_point not in self.decision_tree: # Есть ли текущий путь в дереве решений
                        self.decision_tree.add_node(current_point, lower_bound=int(total_lower_bound)) # Добавление узла с новой нижней границей
                    else:
                        self.decision_tree.nodes[current_point]['lower_bound'] = int(total_lower_bound) # Обновление узла

                    if not self.decision_tree.has_edge(previous_point, current_point): # Проверяет существование направленного ребра
                        self.decision_tree.add_edge(previous_point, current_point) # Добавление ребра
                    
                    self.choosing_path_value(new_path, total_value + re_value, new_re_matrix, current_point) # Вызов функции для продолжения пути

    def solve(self):
        re_matrix, re_value = self.matrix_reduction(self.matrix) # Присваивание редуцированной матрицы

        self.decision_tree.add_node("Начало", label="Начало") # Создание начального узла

        self.choosing_path_value([0], re_value, re_matrix, "Начало") # Поиск пути

        return self.optimal_path, self.optimal_value  # Возвращаем только путь и стоимость

class Testing(): # Проверка
    def test(self):
        matrix = [  # Матрица
            [0, 5, 15, 7],
            [9, 0, 20, 10],
            [15, 20, 0, 11],
            [12, 6, 8, 0]
        ]

        start = Logic(matrix) # Загрузка матрицы
        path, value = start.solve() # Запуск функции решения
        
        full_path = " -> ".join([chr(65 + point) for point in path]) # Преобразование данных в путь

        print(f"Полный путь: {full_path}") # Вывод полного минимального пути
        print(f"Минимальная стоимость пути: {value}") # Вывод минимальной стоимости

if __name__ == "__main__": # Запуск тестирования
    decision = Testing() # Присваивание класса для избежания ошибки
    decision.test() # Запуск теста