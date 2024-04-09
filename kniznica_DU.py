import psycopg2
from author import Author
from book import Book
from genre import Genre
from member import Member
from loan import Loan

conn = psycopg2.connect(
    dbname='bva2e94t1hjabargw4qm',
    user='uoxfcfn6z1ax4uvdhs8d',
    password='BqNof4FiTkz7VmAFcWYqzxjR5vMqRv',
    host='bva2e94t1hjabargw4qm-postgresql.services.clever-cloud.com',
    port='50013'
)

cursor = conn.cursor()

def vypis_menu():
    print("1. Pridať autora")
    print("2. Pridať žáner")
    print("3. Pridať knihu")
    print("4. Zmazať knihu z databázy")
    print("5. Vyhľadať knihu")
    print("6. Zaregistrovať nového člena knižnice")
    print("7. Zmazať existujúceho člena knižnice")
    print("8. Požičať knihu registrovanému členovi")
    print("9. Zobraziť výpožičky člena")

def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vaša možnosť: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
        elif choice == "3":
            Author.zobraz_autorov(cursor)
            authorID = input("ID Autora: ")
            Genre.zobraz_zanre(cursor)
            genreID = input("ID Žánru: ")
            Book.vloz_do_db(cursor, authorID, genreID)
            conn.commit()
        elif choice == "4":
            Book.vymaz_knihu(cursor)
            conn.commit()
        elif choice == "5":
            Book.vyhladaj_knihu(cursor)
        elif choice == "6":
            Member.register_member(cursor)
            conn.commit()
        elif choice == "7":
            Member.delete_member(cursor)
            conn.commit()
        elif choice == "8":
            Loan.pozicat_knihu(cursor)
            conn.commit()
        elif choice == "9":
            Loan.zobraz_vypozicky(cursor)
        else:
            print("Neplatný vstup")

aplikacia()
