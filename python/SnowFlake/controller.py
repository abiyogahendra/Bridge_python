from config import mysql
from flask import jsonify
import pymysql
from app import app

app.app_context().push()
def datasets():
    
	try:
		conn = mysql.connect() #membuat sebuah penghubung dengan fungsi mysql.connect
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT class, text as sentence FROM datasets") # mengambil data dari datasets dengan column class dan text
		rows = cursor.fetchall()
		return rows
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

def insert(classN, text):
	try:
		sql = "INSERT INTO datasets(class, text) VALUES(%s, %s)" #digunakan untuk melakukan insert kedalam data base dengan nama variable sql
		data = (classN, text) #Melakukan pemindahan argument yaitu classN dan text
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('User added successfully!')
		resp.status_code = 200
		return resp

	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

def historyDetection(username, tweet, classN, classification):
	try:
		sql = "INSERT INTO history_detection(username, tweet, class, classification) VALUES(%s, %s, %s, %s)"
		data = (username, tweet, classN, classification)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('successfully!')
		resp.status_code = 200
		return resp

	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
