class Member:
    @staticmethod
    def register_member(cursor):
        print("Vlozte meno: ")
        meno = input()
        print("Vlozte priezvisko: ")
        priezvisko = input()
        print("Vlozte email: ")
        email = input()
        cursor.execute("INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s)", (meno, priezvisko, email))
        print("Člen bol úspešne zaregistrovaný.")

    @staticmethod
    def delete_member(cursor):
        print("Zadajte ID člena, ktorého chcete vymazať: ")
        member_id = input()
        cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
        print("Člen bol úspešne vymazaný.")
