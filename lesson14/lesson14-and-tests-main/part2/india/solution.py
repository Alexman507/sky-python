import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("select `type`, COUNT(*) "
                "FROM netflix "
                "WHERE country LIKE '%India%' "
                "GROUP BY `type`")
cur.execute(sqlite_query)
result = cur.fetchall()
movies_count = result[0][1]
tv_show_count = result[1][1]
result = f'фильмы: {movies_count} шт\nсериалы: {tv_show_count} шт'
con.close()

if __name__ == '__main__':
    print(result)
