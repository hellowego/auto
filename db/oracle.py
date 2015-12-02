#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import cx_Oracle as orcl

if __name__ == "__main__":
	print(orcl.clientversion())
	# conn = cx_Oracle.connect('uopsett_b_xz/uopsett@192.168.109.2/xz_test')
	username = "uopsett_b_xz"
	passwd = "uopsett"
	host = "192.168.109.2"
	port = "1521"
	sid = "xzttest"
	dsn = orcl.makedsn(host, port, sid)
	con = orcl.connect(username, passwd, dsn)

	cursor = con.cursor()
	sql = "SELECT * FROM tp_dealtime"
	cursor.execute(sql);
	result = cursor.fetchall()
	print("Total: " + str(cursor.rowcount))

	for row in result:
		print(row)
		print row[1]

	cursor.close()
	con.close()

	print(orcl.Date(2015,3,13))
