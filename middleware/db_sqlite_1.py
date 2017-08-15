#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('C:\Dev\sqlite\demo.db')

print "Opened database successfully";

cursor = conn.execute("select a, b from first")

for row in cursor:
	print "a = ", row[0]
	print "b = ", row[1]

print "Operation done sucessfully";
conn.close()
