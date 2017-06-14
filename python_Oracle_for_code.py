#--------------------output uuid-------------------------
import uuid

def my_random_uuid(string_length=32):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

print(my_random_string())

#-----------connect to database and set SQL---------------
import cx_Oracle
from sys import modules

# set and build connection
connect_str = u'TNS'
connection = cx_Oracle.connect(connect_str)
cursor = connection.cursor()

# update data
statement = ("UPDATE table_name SET code = :1 WHERE code = :2")
cursor.execute(statement, ('1-DOC-2017-11-00011', '1-DOC-2017-77-00077'))
connection.commit()

# print result to check
cursor.execute(u'select CODE, DN_CARDNO, REMARK from table_name')
for row in cursor:
    print row[0], "-", row[1].encode('utf8'), row[2].encode('utf8')

# close connection
connection.close()
