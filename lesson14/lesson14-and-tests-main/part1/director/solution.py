import sqlite3
import prettytable


con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT DISTINCT `director` "
                "FROM netflix ")
result = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
