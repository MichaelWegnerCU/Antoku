import csv, sqlite3
conn = sqlite3.connect("testtest.db")
curs = conn.cursor()
curs.execute("CREATE TABLE Address (street_address TEXT, zipcode INTEGER, zillow_id INTEGER PRIMARY KEY, Zestimate INTEGER, HomeType TEXT, NumBath INTEGER, NumBed INTEGER, HomeSize INTEGER, LNG REAL, LAT REAL);")
reader = csv.reader(open('UpdatedHomeLatLong.txt', 'r'), delimiter='|')
for row in reader:
    to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]]
    curs.execute("INSERT INTO Address (street_address, zipcode, zillow_id, Zestimate, HomeType, NumBath, NumBed, HomeSize, LNG, LAT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()