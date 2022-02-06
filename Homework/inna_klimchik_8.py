empty_list = []
for _ in range(0, 5):                                               # Создаем массив
    empty_list.append([' ', ' ', ' ', ' ', ' '])
for i in range(0, len(empty_list)):                                 # Вывод пустой таблицы
    print("*---*---*---*---*---*")                                          # Верхний разделитель
    border = '| '                                                   # Левая стенка
    border += ' | '.join(empty_list[i]) + ' |'                      # Заключение ячеек в границы
    print(border)                                                   # Вывод готовой строки с данными и границами
print("*---*---*---*---*---*")                                              # Нижний разделитель

while True:                                                         # Вывод меню с выбором действия
    print("\n1) Сделать запись \n"
          "2) Получить значение по координатам \n"
          "3) Показать все ячейки \n"
          "4) Удалить значение по координатам \n"
          "0) Программа завершает работу.")
    choice = int(input("Выбери действие: "))                        # Поставила в конец этот текст, чтобы пользователю
                                                                    # было очевидно, куда вводить значение
    if choice == 1:                                                 # Действие с записью ячейки
        coordinates = input("\nВведите x и y в формате x=2;y=2;value='v': ")    # Ввод координат
        x_axis = int(coordinates.split(";")[0].split("=")[1])       # Сплитуем и выбираем элемент для х координаты
        y_axis = int(coordinates.split(";")[1].split("=")[1])       # Сплитуем и выбираем элемент для у координаты
        value = coordinates.split(";")[2].split("=")[1][1]          # Сплитуем и выбираем элемент для value без кавычек
        if empty_list[y_axis][x_axis] == " ":                       # Проверяем пустая ли ячейка
            empty_list[y_axis][x_axis] = value                      # Записываем
        else:
            while True:                                             # Если не пустая спрашиваем перезаписать ли её
                rewrite = int(input('Ячейка занята! Перезаписать? \n 1) Да \n 2) НЕТ! \n'))
                if rewrite == 1:
                    empty_list[y_axis][x_axis] = value              # Если 1 то перезаписать и вывести нужный текст
                    print('Запись сделана! \n')
                    break                                           # Прервать цикл вопросов да/нет
                elif rewrite == 2:                                  # Если 2 то просто прервать цикл
                    break
                else:
                    continue                                        # Если не указать 1/2 цикл попросит выбрать еще раз
                                                                    # что делать с ячейкой
    if choice == 2:                                                 # Действие с выводом значения ячейки по координатам
        coordinates = input("\nВведите x и y в формате x=2;y=2: ")  # Ввод координат
        x_axis = int(coordinates.split(";")[0].split("=")[1])
        y_axis = int(coordinates.split(";")[1].split("=")[1])
        if empty_list[y_axis][x_axis] == " ":                       # Если ячейка пустая пишем об этом
            print("пустая ячейка \n")
        else:
            print(empty_list[y_axis][x_axis])                       # Если в ней что то есть, выводим это

    if choice == 3:                                                 # Действие с отображением таблицы и её содержимого
        empty_list.reverse()                                        # Чтобы система координат имела центр, как в домашке
                                                                    # дважды переворачиваем список со строками
        for i in range(0, len(empty_list)):
            print("*---*---*---*---*---*")
            border = '| '
            border += ' | '.join(empty_list[i]) + ' |'
            print(border)
        print("*---*---*---*---*---*")
        empty_list.reverse()

    if choice == 4:                                                 # Действие с удалением записи в ячейке
        coordinates = input("\nВведите x и y в формате x=2;y=2: ")  # Ввод координат
        x_axis = int(coordinates.split(";")[0].split("=")[1])
        y_axis = int(coordinates.split(";")[1].split("=")[1])
        empty_list[y_axis][x_axis] = " "                            # Перезапись ячейки пустым полем
        print("Запись удалена!\n")
    elif choice == 0:                                               # Завершение программы
        break
    else:
        continue                                                    # При некорректном вводе, повторный вывод меню
