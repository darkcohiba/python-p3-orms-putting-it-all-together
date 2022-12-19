import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:

    def __init__(self, name, breed):
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