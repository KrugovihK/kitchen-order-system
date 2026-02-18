def check_my_kitchen():
    """
    Функция с вводом данных от пользователя
    """
    print("Проверка размеров кухни")
    
    # Ввод данных
    length = float(input("Введите длину кухни (в метрах): "))
    width = float(input("Введите ширину кухни (в метрах): "))
    
    # Расчет и вывод
    area = length * width
    print(f"Площадь вашей кухни: {area} кв.м")
    
    if area < 6:
        print("Это маленькая кухня")
    elif area < 10:
        print("Это средняя кухня")
    else:
        print("Это большая кухня")

# Запуск
check_my_kitchen()
