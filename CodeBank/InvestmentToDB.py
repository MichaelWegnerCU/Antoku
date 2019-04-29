import csv, sqlite3
conn = sqlite3.connect("testtest.db")
curs = conn.cursor()
curs.execute("CREATE TABLE Investment (investmentId INTEGER PRIMARY KEY, status TEXT, antoku_number INTEGER);")
reader = csv.reader(open('InvestmentID.csv', 'r'), delimiter=',')
for row in reader:
    to_db = [row[0], row[1], row[2]]
    curs.execute("INSERT INTO Investment (investmentId, status, antoku_number) VALUES (?, ?, ?);", to_db)
conn.commit()