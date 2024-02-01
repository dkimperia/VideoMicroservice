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
print(server.config["MYSQL_HOST"])