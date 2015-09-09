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


conn = mysql.connect()

cur = conn.cursor()

code = 12345

# cur.execute('SELECT * FROM codes WHERE code = ' + code + '') 
sid = '26015900'
code = 12345
# cur.execute('UPDATE codes SET used = 1, student_id = %s WHERE code = %s', (sid, code))
cur.execute("SELECT * FROM codes WHERE code = %s", (code,))
code_data= cur.fetchone()

print(code_data)
