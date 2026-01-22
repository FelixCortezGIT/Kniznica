class Book:
    def __init__(self, name, author, isbn, year, available=True):
        self.attributes(name, author, isbn, year, available)

    def attributes(self, name, author, isbn, year, available):
        self.name = str(name)
        self.author = str(author)
        self.isbn = int(isbn)
        self.year = int(year)
        self.available = available
        return self

    def lend(self):
        if self.available:
            self.available = False
            return True
        return False

    def returning(self):
        self.available = True
        return True

    def __str__(self):
        state="dostupna" if self.available else "nedostupna"
        return f"{self.name} od {self.author}, ISBN:{self.isbn}, Rok vydania {self.year}, {state}"

# class Library:
#     def adding(self):
#
#     def search(self):
#
#     def lend(self):
#
#     def returning(self):
#
#     def showme(self):

book1 = Book("Harry Potter", "Rowlings", 11221133, 2010)
book2 = Book("Pan Prstenov", "Tolkien", 11223344, 2003)
book3 = Book("Patriot Games", "Tom Clancy", 33221133, 1987)
book4 = Book("Chromosome 6", "Robin Cook", 22113344, 1992)
book5 = Book("The Client", "John Grisham", 22443311, 1993)
book6 = Book("Stained White Radiance", "James Lee Burke", 33113311, 1992)
print(book3)
