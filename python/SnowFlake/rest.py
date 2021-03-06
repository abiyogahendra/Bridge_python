import pymysql
import werkzeug
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import security
from werkzeug.security import generate_password_hash, check_password_hash
from ANN import classify 
from controller import historyDetection
from helper import removeEmoji
		
@app.route('/check', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO user_table(user_name, user_email, user_password) VALUES(%s, %s, %s)" #insert data yang sudah di ambil ke dalam database
			data = (_name, _email, _hashed_password,) #dengan memasukkan argument name, email, hashed pass
			conn = mysql.connect() #membuat koneksi sementara dengan database
			cursor = conn.cursor()
			cursor.execute(sql, data) #mengeksekusi data query dengan memasukkan argument dari objek data
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM user_table")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/datasets')
def datasets():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM datasets")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/manual', methods=['POST'])
def manual():
	_json = request.json
	_tweet = _json['tweet']

	tweetNoEmoji = removeEmoji(_tweet)
	classifyT = classify(tweetNoEmoji)

	resp = jsonify(classifyT)
	resp.status_code = 200
	return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
