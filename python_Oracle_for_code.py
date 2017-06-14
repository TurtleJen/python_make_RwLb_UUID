#--------------------output uuid-------------------------
import uuid

def my_random_uuid(string_length=32):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

print(my_random_uuid())

#-----------connect to database and set SQL---------------
import cx_Oracle
from sys import modules

# set and build connection
connect_str = u'TNS'
connection = cx_Oracle.connect(connect_str)
cursor = connection.cursor()

#-----------------------查出欄位值------------------------undo
cursor.execute(u'select CODE, DN_CARDNO, REMARK from table_name')
for row in cursor:
    print row[0], row[1].encode('utf8'), row[2].encode('utf8')

#-------塞進陣列集合，增加一個值是兩欄位相加中間底線------undo
data_set={row_list}
row_list=[]


data_set.add(row_list)

#--------------------將陣列update進table------------------undo
# update data
# statement = ("UPDATE table_name SET code = :1 WHERE code = :2")
# cursor.execute(statement, ('1-DOC-2017-11-00011', '1-DOC-2017-77-00077'))
# connection.commit()

#-------------------------確認結果------------------------
# print result to check
# cursor.execute(u'select CODE, DN_CARDNO, REMARK from table_name')
# for row in cursor:
#     print row[0], "-", row[1].encode('utf8'), row[2].encode('utf8')

# close connection
connection.close()

#---source----------
# https://sites.google.com/site/zsgititit/home/python-cheng-shi-she-ji/python-zi-liao-chu-cun-rong-qituple-chuan-lie-zi-dian-ji-he
# http://icodding.blogspot.tw/2016/05/python-listtuplestringdictset.html
# http://design2u.me/blog/33/python-list-%E4%B8%B2%E5%88%97-%E8%88%87-dictionary-%E5%AD%97%E5%85%B8-%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4
# http://tech-marsw.logdown.com/blog/2014/09/03/getting-started-with-python-in-ten-minute
# python3.5 
#    https://docs.python.org.tw/3/library/array.html
# python 2.7
#    https://docs.python.org/2/library/array.html
# https://crazyof.me/blog/archives/689.html
