import mysql.connector as sl 

def create_RMS():

    con = sl.connect(
        host="localhost",
        user="root",
        passwd="12345"   
    )
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS RMS")
    con.commit()
    con.close()

def get_connection():
    return sl.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="RMS"
    )
