import sqlite3
from flask import Flask, flash




app = Flask(__name__)
app.config.from_object('config')



if __name__ == '__main__':
	app.run()