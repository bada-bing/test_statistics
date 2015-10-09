__author__ = 'Milan'

import odbchelper
import connection
import sys

#print(odbchelper.buildConnectionString.__doc__)

#print(sys.path)

(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) = range(7)

print("Danas je " + str(Tuesday))

connection.connect()



