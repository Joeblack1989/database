import r_w_file
import working_file
import action_table

path_txt = 'base_data.txt'
data = r_w_file.read_file(f'{path_txt}')
action_table.output_all(data)

working_file.append_info(data,path_txt)
action_table.output_all(data)

working_file.del_info(data,path_txt)
action_table.output_all(data)


# 1. Работа с файлом (Вход Файл - Выход словарь)
# 2. Работа с данными (Вход Множество, Значение для действия - Выход Печать)
# Вывод учеников определенного класса
# Вывод учеников по Алфавиту по фамилии
# 3. Пользовательский интерфейс (Вход Пользовательский - Возвращает значение для действия)
# 4. "Кнопка" (Сбор структуры модулей)




