import mysql.connector
test=mysql.connector.connect(host='localhost',username='root',password='243203',database='srms')
cur=test.cursor()
s="CREATE TABLE book_phir_se(bookid INTEGER,title VARCHAR(20),price FLOAT(5,2))"
cur.execute(s)
print("hello")

