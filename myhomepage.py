import pymysql
import pyodbc
server = 'youngheewebdb.database.windows.net'
username = 'tjdudgml3'
password = 'tjdudgml123!!'
database= 'myWebsiteDB'
driver= '{ODBC Driver 17 for SQL Server}'


def insert_guestbook_click():
    id_label = 1
    if id_label is None:
        pass
        #alert("id를 입력해주세요!")
    else:
        return True

if insert_guestbook_click():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            id_label = 'guest3'
            email_label = '123@naver.com'
            comment_label = 'test'
            
            # query = "INSERT INTO MyWebsite.guest(ID, email, contents ) VALUES('guest1', '123@naver.com', 'test');"
            query = "INSERT INTO MyWebsite.guest(ID, email, contents ) VALUES(?, ?, ?);"
            cursor.execute(query,id_label, email_label, comment_label)
            # query = 
            # table = cursor.fetchall()
            # for a in table:
            #     print(a)
    #df = pd.read_sql(SQL,db)

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        query = "SELECT * FROM MyWebsite.guest"
        cursor.execute(query)
        table = cursor.fetchall()
        for a in table:
            print(a)