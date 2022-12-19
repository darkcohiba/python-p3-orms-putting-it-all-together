import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    
