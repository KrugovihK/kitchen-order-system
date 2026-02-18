class Material:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def info(self):
        return f"{self.name}: {self.price} руб/м"

# Создаем материалы
wood = Material("Дерево", 5000)
plastic = Material("Пластик", 1500)
glass = Material("Стекло", 3000)

# Используем
print(wood.info())      # Дерево: 5000 руб/м
print(plastic.info())   # Пластик: 1500 руб/м
print(glass.info())     # Стекло: 3000 руб/м
