import sqlite3 as db


con = db.connect("demo.db") 

con.execute('create table if not exists data(pwd varchar(255))') 

con.commit()