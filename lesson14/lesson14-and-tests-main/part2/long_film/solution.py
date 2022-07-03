import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT `title`, MAX(duration) "
                "FROM netflix "
                "WHERE release_year=2019 "
                "AND type='Movie'")
cur.execute(sqlite_query)
result = cur.fetchall()
movie_title = result[0][0]
duration = result[0][1]
result = (f'{movie_title} — {duration} минут')

if __name__ == '__main__':
    print(result)
