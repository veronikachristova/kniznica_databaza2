class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_year, copies):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies

    @classmethod
    def from_db(cls, value):
        # Zistíme, či máme dostatok údajov
        if len(value) >= 7:
            return cls(value[0], value[1], value[2], value[3], value[4], value[5], value[6])
        else:
            # Ak nie, použijeme predvolené hodnoty alebo inú vhodnú alternatívu
            print("Nie všetky údaje o knihe boli získané z databázy.")
            return None

    @staticmethod
    def vloz_do_db(cursor, author_id, genre_id):
        print("Vlozte nazov knihy ")
        title = input()
        print("Vlozte ISBN: ")
        isbn = input()
        print("Vlozte rok vydania: ")
        publication_year = input()
        print("Vlozte pocet kusov: ")
        copies = input()
        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn, publication_year, copies) VALUES (%s, %s, %s, %s, %s, %s)",
                       (title, author_id, genre_id, isbn, publication_year, copies))

    @staticmethod
    def vymaz_knihu(cursor):
        print("Zadajte ID knihy, ktorú chcete vymazať: ")
        book_id = input()
        cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
        print("Kniha bola úspešne vymazaná.")

    @staticmethod
    def vyhladaj_knihu(cursor):
        print("Zadajte kritéria pre vyhľadávanie knihy:")
        criterion = input("1. Názov\n2. Autor\n3. Žáner\nZadajte číslo kritéria: ")
        if criterion == "1":
            title = input("Zadajte názov knihy: ")
            cursor.execute("SELECT * FROM books WHERE title = %s", (title,))
        elif criterion == "2":
            author_name = input("Zadajte meno autora knihy: ")
            cursor.execute("SELECT * FROM books JOIN authors ON books.author_id = authors.author_id WHERE authors.name = %s",
                           (author_name,))
        elif criterion == "3":
            genre_name = input("Zadajte názov žánru knihy: ")
            cursor.execute("SELECT * FROM books JOIN genres ON books.genre_id = genres.genre_id WHERE genres.name = %s",
                           (genre_name,))
        else:
            print("Neplatný vstup.")
            return
        books = cursor.fetchall()
        if not books:
            print("Žiadne knihy neboli nájdené podľa zadaných kritérií.")
        else:
            for book in books:
                print(Book.from_db(book))

    def __str__(self):
        return f"---KNIHA---\nID Kniha: {self.id}\nNázov: {self.title}\nID Autora: {self.author_id}\nID Žánru: {self.genre_id}\nISBN: {self.isbn}\nRok vydania: {self.publication_year}\nPocet kusov: {self.copies}"
