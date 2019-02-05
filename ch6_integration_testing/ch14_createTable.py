
import sqlite3
import time
import datetime
import random

#-----------------------------------------------------------------------------
#                   CHAPTER 14 - REAL WORLD APPLICATIONS
#-----------------------------------------------------------------------------

#------------------------TASK 1 - CREATE A TABLE + INSERT DATA---------------

conn = sqlite3.connect("task1.db")

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

#def data_entry():
#    c.execute("INSERT INTO StuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
#    conn.commit()
#    c.close()
#    conn.close()

create_table()
#data_entry()

#------------------------TASK 2 - ADD DATA TO TABLE USING VARIABLES---------------

def dynamic_data_entry():
    unix = time.time()
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = "python"
    value = random.randrange(0,10)
    c.execute('INSERT INTO StuffToBuild(unix, datestamp, keyword, value) VALUES (?,?,?,?)', (unix, datestamp, keyword, value))
    conn.commit()
    
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

#------------------------TASK 3 - READ AND SELECT DATA FROM A DATABASE---------------


def read_from_db_all():
    c.execute("SELECT * FROM stuffToBuild WHERE value = 8 ")
    for row in c.fetchall():
        print(row)

read_from_db_all()


def read_from_db2():
   c.execute("SELECT * FROM stuffToBuild WHERE value = 8 and unix>1547029682  and unix < 1547030011 ")
   for row in c.fetchall():
       print(row[1])  
       
read_from_db2()
c.close()
conn.close()
 
    
    
    
    
    
    
    
    
    
