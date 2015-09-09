#!flask/bin/python
from flask import Flask, request, jsonify, json, render_template, abort
import time

from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ninja'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config["JSON_SORT_KEYS"] = True #otherwise it's alphabetical
mysql.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/all')
def get_all():
	cur = mysql.get_db().cursor() 
	cur.execute('SELECT * FROM codes')

	codes = cur.fetchall();

	codes_dict = []
	for code in codes:
		code_dict = {
				'code_id': code[0],
				'code': code[1],
				'used': code[2],
				'student_id': code[3],
				}
		codes_dict.append(code_dict)

	return jsonify(data = codes_dict)

@app.route('/get', methods=['POST'])
def get():
	conn = mysql.connect();

	cur = conn.cursor()

	try:
		cur.execute("SELECT * FROM codes WHERE code = %s", (request.json['code'],)) 
		code_data= cur.fetchone()
		print code_data

		code = {
				'code_id': code_data[0],
				'code': code_data[1],
				'used': code_data[2],
				'student_id': code_data[3],
				}

		print request.json['code']
		print request.json['student_id']

		cur.execute("SELECT * FROM codes WHERE student_id = %s", (request.json['student_id'],))
		sid_data = cur.fetchone()

		# If successful, generate a random coupon_code and put it in the database, if not more than X coupon_codes have been generated for this particular code, otherwise throw an error :(
		used =  code['used'] 
		print used
		print sid_data
		if used == 0 and sid_data is None:
			cur.execute("UPDATE codes SET used = 1, student_id = %s WHERE code = %s", (request.json['student_id'], request.json['code'],))
			conn.commit();
			return jsonify({"status":"success"})
		else:
			return jsonify({"status":"error"})

	except:
		return jsonify({"status":"error2"})
	

if __name__ == '__main__':
    app.run(debug=True)
