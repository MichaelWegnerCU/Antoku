import csv, sqlite3
conn = sqlite3.connect("AddressToDB.db")
curs = conn.cursor()
curs.execute("CREATE TABLE Address (street_address TEXT, zipcode INTEGER, zillow_id INTEGER PRIMARY KEY, Zestimate INTEGER, HomeType TEXT, NumBath INTEGER, NumBed INTEGER, HomeSize INTEGER);")
reader = csv.reader(open('AdressDatabase.txt', 'r'), delimiter='|')
for row in reader:
    to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
    curs.execute("INSERT INTO Address (street_address, zipcode, zillow_id, Zestimate, HomeType, NumBath, NumBed, HomeSize) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()