import pymysql
import pyodbc
server = 'youngheewebdb.database.windows.net'
username = 'tjdudgml3'
password = 'tjdudgml123!!'
database= 'myWebsiteDB'
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        query = "SELECT * FROM MyWebsite.guest"
        cursor.execute(query)
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]) + " "+ str(row[2]))
            row = cursor.fetchone()


