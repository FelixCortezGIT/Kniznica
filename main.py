class Book:
    def __init__(self, name, author, isbn, year, available=True):
        self.attributes(name, author, isbn, year, available)
    def attributes(self, name, author, isbn, year, available):
        self.name = str(name)
        self.author = str(author)
        self.isbn = int(isbn)
        self.year = int(year)
        self.available = bool(available)
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
        state = "dostupna" if self.available else "vypozicana"
        return f"{self.name} od {self.author}, ISBN: {self.isbn}, Rok vydania: {self.year}, {state}"

class Library:
    def __init__(self):
        self.books = []
    def adding(self, book):
        if all(b.isbn != book.isbn for b in self.books):
            self.books.append(book)
            return True
        return False
    def search(self, name):
        name = str(name).lower()
        return [b for b in self.books if name in b.name.lower()]
    def lend(self, isbn):
        isbn = int(isbn)
        for b in self.books:
            if b.isbn == isbn:
                return b.lend()
        return False
    def returning(self, isbn):
        isbn = int(isbn)
        for b in self.books:
            if b.isbn == isbn:
                b.returning()
                return b
        return None
    def showme(self):
        available_books = [b for b in self.books if b.available]
        for b in available_books:
            print(b)
        return available_books

book1 = Book("Harry Potter", "Rowlings", 11221133, 2010)
book2 = Book("Pan Prstenov", "Tolkien", 11223344, 2003)
book3 = Book("Patriot Games", "Tom Clancy", 33221133, 1987)
book4 = Book("Chromosome 6", "Robin Cook", 22113344, 1992)
book5 = Book("The Client", "John Grisham", 22443311, 1993)
book6 = Book("Stained White Radiance", "James Lee Burke", 33113311, 1992)

print()
print(book3)

library = Library()
library.adding(book1)
library.adding(book2)
library.adding(book3)
library.adding(book4)
library.adding(book5)
library.adding(book6)

library.lend(33221133)
library.lend(11223344)
print()
print(book2)
print(book3)

print()
print("dostupne knihy:")
library.showme()

print()
print("hladam knihu podla retazca: radiance")
for b in library.search("radiance"):
    print(b)

returned = library.returning(11223344)
print()
if returned:
    print(f"po vrateni knihy: {returned.name} je stav kniznice nasledovny:")
    library.showme()
else:
    print("knihu s danym ISBN sa nepodarilo najst")
