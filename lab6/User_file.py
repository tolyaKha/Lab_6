import pymysql as MySQLdb


class Connection:

    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection (self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )
    def disconnect(self):
        if self._connection:
            self._connection.close()

class Book:
    def __init__(self, db_connection, name, discription):
        self.db_connection = db_connection.connection
        self.name=name
        self.discription = discription

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO books (name, discription) VALUES (%s, %s);",
                  (self.name, self.discription))
        self.db_connection.commit()
        c.close()

con = Connection("admin", "12345", "first_db")

with con:
    book = Book(con, 'New book','Discription new book')
    book.save()
