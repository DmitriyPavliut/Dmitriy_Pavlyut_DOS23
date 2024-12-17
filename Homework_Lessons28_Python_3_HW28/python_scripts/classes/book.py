class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"{self.title} - {self.author}, {self.year}"

    def set_year(self, new_year):
        self.year = new_year