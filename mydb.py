# # steps done are
# # install mysql on pc
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mysql123+'
)

# prepare a cursors object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print('all done!')
