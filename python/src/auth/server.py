import jwt, datetime, os
from flask import Flask, request
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import pymysql


server = Flask(__name__)
#object of Flask class
pymysql.install_as_MySQLdb()
mysql = MySQL(server)

#config
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
# print(server.config["MYSQL_HOST"])
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

#marshrut
@server.route("/login", method=["POST"])
def login():
	auth = request.authorization
	if not auth:
		return "missing credentials", 401

	#check db for username and password
	cur = mysql.connection.cursor()

	res = cur.execute(
		"SELECT email, password FROM user WHERE email=%s", (auth.username,)

	)

	if res > 0:
		user_row = cur.fetchone()
		email = user_row[0]
		password = user_row[1]

		if auth.username != email or auth.password != password:
			return "Invalid credentials", 401
		else:
			return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)#check JWT

	else:
		return "Invalid credentials", 401


@server.route("/validate", method=["POST"])
def validate():
	encoded_jwt = request.headers["authorization"]

	if not encoded_jwt:
		return "missing credentials", 401

	encoded_jwt = encoded_jwt.split(" ")[1]
	try:
		decode = jwt.decode(
			encoded_jwt, os.environ.get("JWT_SECRET"), algorithm=['HS256']
		)
	except:
		return 'not authorized', 403 

	return decoded, 200



#True or false admin or net
def createJWT(username, secret, authz):
	return jwt.encode(
		{
			"username": username,
			"exp": datetime.datetime.now(tz=datetime.timezone.utc)
			+ datetime.timedelta(days = 1),
			"iat": datetime.datetime.utcnow()
			"admin": authz,
		},
		secret,
		algorithm = "HS256"
	)

if __name__ == "__main__":
	server.run(host = "0.0.0.0", port = 5000)








