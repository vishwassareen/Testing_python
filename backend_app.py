import psycopg2


def connect():
    con = psycopg2.connect("dbname= 'python_test' user='********' password='******' host='localhost' port='5432'")   
    cur=con.cursor()
    cur.execute(" CREATE TABLE if not exists book (id serial PRIMARY KEY, title text , author text, year integer, isbn integer) ")
    con.commit()
    con.close()

def insert(title,author,year,isbn):
    con = psycopg2.connect("dbname= 'python_test' user='********' password='******' host='localhost' port='5432'") 
    cur=con.cursor()
    statement=""" Insert into book (title,author,year,isbn) VALUES(%s,%s,%s,%s)"""
    record=(title,author,year,isbn)
    cur.execute(statement,record)
    con.commit()
    con.close()

def view():
    con = psycopg2.connect("dbname= 'python_test' user='********' password='******' host='localhost' port='5432'")
    cur=con.cursor()
    query="""select * from book"""
    cur.execute(query)
    rows=cur.fetchall()
    con.close()
    return rows

def update(id,title,author,year,isbn):
    con = psycopg2.connect("dbname= 'python_test' user='********' password='******' host='localhost' port='5432'") 
    cur=con.cursor()
    query="""update book set title=%s ,author=%s ,year=cast(%s as integer) ,isbn=cast(%s as integer) where id= %s """
    record=(title,author,year,isbn,id)
    cur.execute(query,record)
    con.commit()
    con.close()
    

def search(title="",author="",year="",isbn=""):
    con = psycopg2.connect("dbname= 'python_test' user='********' password='******' host='localhost' port='5432'") 
    cur=con.cursor()
    query=""" select * from book where title=%s or author=%s or cast(year as varchar)=%s or cast(isbn as varchar)=%s """
    rec=(title,author,year,isbn)
    cur.execute(query,rec)
    rows=cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = psycopg2.connect("dbname= 'python_test' user='********' password='******' host='localhost' port='5432'") 
    cur=con.cursor()
    query=""" delete from book where id=%s """
    rec=(id,)
    cur.execute(query,rec)
    con.commit()
    con.close() 


