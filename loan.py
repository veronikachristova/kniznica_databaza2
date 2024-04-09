class Loan:
    @staticmethod
    def pozicat_knihu(cursor):
        print("Zadajte ID člena: ")
        member_id = input()
        print("Zadajte ID knihy: ")
        book_id = input()
        cursor.execute("INSERT INTO loans (book_id, member_id) VALUES (%s, %s)", (book_id, member_id))
        print("Kniha bola úspešne požičaná.")

    @staticmethod
    def zobraz_vypozicky(cursor):
        print("Zadajte ID člena: ")
        member_id = input()
        cursor.execute("SELECT * FROM loans WHERE member_id = %s", (member_id,))
        loans = cursor.fetchall()
        if not loans:
            print("Tento člen nemá žiadne výpožičky.")
        else:
            for loan in loans:
                print(f"Kniha ID: {loan[1]}, Dátum výpožičky: {loan[3]}, Dátum splatnosti: {loan[4]}, Dátum vrátenia: {loan[5]}")
