__author__ = 'Milan'

import mysql.connector
from mysql.connector import errorcode

def connect():
    try:
      db = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          db="test_db"
      )
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
      db.close()
    else:
        cursor = db.cursor()

        add = ("INSERT INTO table_test "
                   "VALUES (%s, %s)")

        data = (6115, 's')

        cursor.execute(add, data)

        db.commit()

        cursor.close()

        db.close()