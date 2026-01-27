class Book:
    def __init__(self, name, author, isbn, year, available=True):
        self.name = str(name)
        self.author = str(author)
        self.isbn = str(isbn)
        self.year = int(year)
        self.available = bool(available)
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
        for b in self.books:
            if b.isbn == isbn:
                return b.lend()
        return False
    def returning(self, isbn):
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

library = Library()
library.adding(book1)
library.adding(book2)
library.adding(book3)
library.adding(book4)
library.adding(book5)
library.adding(book6)

def show_menu():
    print("KNIZNICA")
    print("1) zobrazit dostupne knihy")
    print("2) vyhladat podla nazvu knihy")
    print("3) vyhladat podla autora")
    print("4) vyhladat podla ISBN")
    print("5) pridat knihu")
    print("6) vypozicat knihu podla ISBN")
    print("7) vratit knihu podla ISBN")
    print("8) nacitaj zo suboru")
    print("9) uloz do suboru")
    print("0) koniec")
def print_books(books, header=None):
    if header:
        print(f"\n{header}")
    if not books:
        print("ziadne knihy na zobrazenie")
        return
    for b in books:
        print("-", b)
def input_int(prompt):
    while True:
        s = input(prompt).strip().lower()
        try:
            return int(s)
        except ValueError:
            print("prosim zadajte cele cislo")
def search_by_author(library, author_query):
    q = str(author_query).lower()
    return [b for b in library.books if q in b.author.lower()]
def search_by_isbn(library, isbn):
    return [b for b in library.books if b.isbn == isbn]
def save_to_file(library, path="kniznica.txt"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("name;author;isbn;year;available\n")
            for b in library.books:
                line = f"{b.name};{b.author};{b.isbn};{b.year};{str(b.available)}\n"
                f.write(line)
        print(f"ulozene do suboru: {path}")
        return True
    except Exception as e:
        print(f"chyba pri ukladani: {e}")
        return False
def load_from_file(library, path="kniznica.txt"):
    plus=0
    jump=0
    fault=0
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print("subor sa nenasiel")
        return 0
    except Exception as e:
        print(f"chyba pri nacitani: {e}")
        return 0
    start_idx = 1 if lines[0].strip().lower().startswith("name;") else 0
    for i, line in enumerate(lines[start_idx:], start=start_idx+1):
        if not line.strip():
            continue
        parts = line.split(";")
        if len(parts) != 5:
            fault += 1
            continue
        name, author, isbn_s, year_s, avail_s = [p.strip() for p in parts]
        try:
            isbn = str(isbn_s)
            year = int(year_s)
            available = str(avail_s).strip().lower() in ("true", "1", "a", "ano", "áno", "y", "yes")
        except ValueError:
            fault += 1
            continue
        ok = library.adding(Book(name, author, isbn, year, available))
        if ok:
            plus += 1
        else:
            jump += 1
    print(f"nacitane zo suboru: {path}")
    print(f"pridane: {plus}, duplicitne ISBN: {jump}, chybne riadky: {fault}")
    return plus

def wait_enter():
    input("\npokracujte stlacenim enter...")
while True:
    show_menu()
    choice = input("zvol moznost: ").strip()
    if choice == "1":
        print("\ndostupne knihy:")
        library.showme()
        wait_enter()
    elif choice == "2":
        q = input("zadaj cast nazvu knihy: ").strip()
        results = library.search(q)
        print_books(results, "hladanie podla nazvu knihy: ")
        wait_enter()
    elif choice == "3":
        q = input("zadaj cast mena autora: ").strip()
        results = search_by_author(library, q)
        print_books(results, "hladanie podla mena autora: ")
        wait_enter()
    elif choice == "4":
        isbn = input("zadaj isbn: ").strip()
        results = search_by_isbn(library, isbn)
        print_books(results, "hladanie podla ISBN: ")
        wait_enter()
    elif choice == "5":
        print("\npridanie novej knihy")
        name = input("nazov knihy: ").strip()
        author = input("meno autora: ").strip()
        isbn = input("ISBN: ").strip()
        year = input_int("rok vydania: ")
        avail = input("je dostupna? (enter = ano / n = nie").strip().lower()
        available = False if avail in ("n", "nie", "no") else True
        added = library.adding(Book(name, author, isbn, year, available))
        if added:
            print("kniha bola pridana")
        else:
            print("knihu sa nepodarilo pridat / ISBN uz existuje")
        wait_enter()
    elif choice == "6":
        isbn = input("zadaj ISBN knihy na vypozicanie: ").strip()
        looked=next((b for b in library.books if b.isbn == isbn), None)
        if looked is None:
            print("kniha s danym ISBN sa nenasla")
        else:
            if library.lend(isbn):
                print("kniha bola vypozicana")
            else:
                print("kniha je uz vypozicana")
        wait_enter()
    elif choice == "7":
        isbn = input("zadaj ISBN knihy na vratenie: ").strip()
        returned = library.returning(isbn)
        if returned:
            print(f"vratene: {returned.name}")
        else:
            print("kniha s danym ISBN sa nenasla")
        wait_enter()
    elif choice == "8":
        way = input("zadaj cestu k suboru (enter=kniznica.txt): ").strip()
        if not way:
            way = "kniznica.txt"
        load_from_file(library, way)
        wait_enter()
    elif choice == "9":
        way = input("zadaj cielovy subor (enter=kniznica.txt): ").strip()
        if not way:
            way = "kniznica.txt"
        save_to_file(library, way)
        wait_enter()
    elif choice == "0":
        break
