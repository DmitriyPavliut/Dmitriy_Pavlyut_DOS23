class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model}, Цвет: {self.color}, Год выпуска: {self.year}"

    def set_color(self, new_color):
        self.color = new_color