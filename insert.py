import sqlite3

conn =sqlite3.connect('test.db')

print("Success")

conn.execute("INSERT INTO TEACHERS VALUES (1"
             ",'James','Kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (2,'Ann','Mwende',43,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (6,'Stacy','Mutheu',49,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (8,'John','Tembo',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (9,'Liz','Rehema',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (15,'Aurelia','Raha',47,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (78,'Hillary','Mundo',55,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (198,'Violet','Njeri',25,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (14,'Kelvin','Kariuki',47,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (13,'Lexine','Ndunda',45,56000.00)")

conn.commit()
print("Successfully inserted records")

conn.close()