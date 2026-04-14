from mssql_python import connect

conn = connect(
    "Server=anchorhealthdb.cw5ezu5fyhr7.us-east-1.rds.amazonaws.com;Database=AnchorHealthDB;Uid=AnchorHealthUser;Pwd=R$4!mZ9@Pq2A;")
cursor = conn.cursor()
cursor.execute("SELECT 1")
print(cursor.fetchall())
conn.close()

import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=anchorhealthdb.cw5ezu5fyhr7.us-east-1.rds.amazonaws.com;"
    "DATABASE=AnchorHealthDB;"
    "UID=AnchorHealthUser;"
    "PWD=R$4!mZ9@Pq2A;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(conn_str, timeout=10)
cursor = conn.cursor()

cursor.execute("SELECT 1")
print(cursor.fetchone())

# import pymysql
#
# conn = pymysql.connect(
#     host="anchorhealthdb.cw5ezu5fyhr7.us-east-1.rds.amazonaws.com",
#     port=3306,
#     user="AnchorHealthUser",
#     password="R$4!mZ9@Pq2A",
#     database="AnchorHealthUser",
#     connect_timeout=10
# )
#
# with conn.cursor() as cur:
#     cur.execute("SELECT 1;")
#     print(cur.fetchone())
