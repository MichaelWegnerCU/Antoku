import csv, sqlite3
conn = sqlite3.connect("testtest.db")
curs = conn.cursor()
curs.execute("CREATE TABLE User (UserID INTEGER PRIMARY KEY, InvestmentID INTEGER, CurrentAmount INTEGER, Returns INTEGER);")
reader = csv.reader(open('UserID.csv', 'r'), delimiter=',')
for row in reader:
    to_db = [row[0], row[1], row[2],row[3]]
    curs.execute("INSERT INTO User (UserID, InvestmentID, CurrentAmount, Returns) VALUES (?, ?, ?,?);", to_db)
conn.commit()