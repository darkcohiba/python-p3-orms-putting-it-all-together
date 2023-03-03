import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:

    def __init__(self, name, breed, id = 1):
        self.id = id
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        CURSOR.execute("CREATE TABLE IF NOT EXISTS dogs(id INTEGER PRIMARY KEY, name TEXT, breed TEXT)")
    
    @classmethod
    def drop_table(self):
        CURSOR.execute("DROP TABLE IF EXISTS dogs")

    def save(self):
        CURSOR.execute("INSERT INTO dogs(name, breed) VALUES (?, ?)", (self.name, self.breed))


    @classmethod
    def create(cls, name, breed):
        dog = cls(name, breed)
        dog.save()
        return dog

    
    @classmethod
    def new_from_db(cls, row):
        dog = cls(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

        return dog

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM dogs
        """

        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM dogs
            WHERE name = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None

        return Dog(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM dogs
            WHERE id = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None

        return Dog(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

    @classmethod
    def find_or_create_by(cls, name=None, breed=None):
        sql = """
            SELECT * FROM dogs
            WHERE (name, breed) = (?, ?)
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name, breed)).fetchone()
        if not row:
            sql = """
                INSERT INTO dogs (name, breed)
                VALUES (?, ?)
            """

        CURSOR.execute(sql, (name, breed))
        return Dog(
            name=name,
            breed=breed,
            id=CURSOR.lastrowid
        )

        # return Dog(
        #     name=row[1],
        #     breed=row[2],
        #     id=row[0]
        # )

    def update(self):
        sql = """
            UPDATE dogs
            SET name = ?,
                breed = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.breed, self.id))