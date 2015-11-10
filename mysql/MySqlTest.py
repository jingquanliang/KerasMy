__author__ = 'jql'

import MySQLdb

try:
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='own',port=3306)
    cur=conn.cursor()
    count=cur.execute("select * from user")
    print 'there has %s rows record' % count

    result=cur.fetchone()
    print result
    # print 'ID: %s info %s' % (result[1],result[2])

    results=cur.fetchmany(5)
    for r in results:
        print r

    cur.close()
    conn.close()
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))