import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("select SUM(duration) "
                "FROM netflix "
                "WHERE director='Alastair Fothergill' "
                "AND `type`='TV Show'")
cur.execute(sqlite_query)
seazons = cur.fetchall()[0][0]
result = ('Длительность всех сериалов режиссера Alastair Fothergill'
          f' составляет {seazons} сезона.')
con.close()

if __name__ == '__main__':
    print(result)
