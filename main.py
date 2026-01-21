class Book:
    def atributes(self, name, author, isbn, available, year):
        self.name = name(str)
        self.author = author(str)
        self.isbn = isbn(int)
        self.available = available(bool)
        self.year = year(int)


    def vypozicat(self):

    def vratit(self):

    def __str__(self):


class Library:
    def pridat(self):

    def vyhladavat(self):

    def vypozicat(self):

    def vratit(self):

    def zozbrazit_knihy(self):

book1 = Book("Harry Potter", "ROwlings", 11221133, 2010)
book2 = Book("Pan Prstenov", "Tolkien", 11223344, 2003)
book3 = Book("Patriot Games", "Tom Clancy", 33221133, 1987)
book4 = Book("Chromosome 6", "Robin Cook", 22113344, 1992)
book5 = Book("The Client", "John Grisham", 22443311, 1993)
book6 = Book("Stained White Radiance", "James Lee Burke", 33113311, 1992)
