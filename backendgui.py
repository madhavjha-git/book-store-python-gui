import sqlite3

class DataBase:

    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists book (id integer primary key,"
                    "title text,author text,year integer,isbn integer)")
        self.conn.commit()
        
    def insert(self,title, author, year, isbn):
        self.cur.execute("insert into book values (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("select * from book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("select * from book where title=? or author=? or year=? or isbn=?"
                    , (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("delete from book where id=?", (id,))
        self.conn.commit()

    def update(self,id, title, author, year, isbn):
        self.cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?", (title, author, year, isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()