#!flask/bin/python
from flask import Flask, request, jsonify, json, render_template, abort

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
				'used': code[2]
				}
		codes_dict.append(code_dict)

	return jsonify(data = codes_dict)

@app.route('/get', methods=['POST'])
def get():
	conn = mysql.connect();

	cur = conn.cursor()

	print request.form

	try:
		cur.execute('SELECT * FROM codes WHERE code = ' + request.json['code']) 
		code_data= cur.fetchone()

		code = {
				'code_id': code_data[0],
				'code': code_data[1],
				'used': code_data[2]
				}

		cur.execute('UPDATE codes SET used = 1 WHERE code = ' + request.json['code'])
		conn.commit();
		
		# If successful, generate a random coupon_code and put it in the database, if not more than X coupon_codes have been generated for this particular code, otherwise throw an error :(

		return jsonify({'status':'success'})

	except:
		return jsonify({"status":"error"})
	

if __name__ == '__main__':
    app.run(debug=True)
