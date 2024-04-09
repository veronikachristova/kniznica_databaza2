class Genre:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte nazov zanru: ")
        name = input()
        print("Vlozte opis zanru: ")
        description = input()
        cursor.execute("INSERT INTO genres (name, description) VALUES (%s, %s)", (name, description))
        print("Zaner vlozeny do databazy.")

    @staticmethod
    def zobraz_zanre(cursor):
        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()
        for genre in genres:
            print(Genre.from_db(genre))

    def __str__(self):
        return f"---ZANER---\nID Zanru: {self.id}\nNazov: {self.name}\nDescription: {self.description}"
