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













