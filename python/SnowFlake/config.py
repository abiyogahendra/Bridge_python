from app import app
from flaskext.mysql import MySQL

# Twitter configurations
ACCESS_TOKEN = "1278260576251076608-AZd9nafiaqpn6Z1Eaq2Qgy9uYFgpBM"
ACCESS_TOKEN_SECRET = "Mf3Jn8h53FNSK0e9DdnBILX6KOSXABKna9rikzLSo7EVL"
CONSUMER_KEY = "MqiWcnuB3qbOh7TGw3Ia54qFB"
CONSUMER_SECRET = "b6QZ4eQwOvJooTPloWTHOGEPKl8wApmeVMs14hyqnHfNsvCRuC"
 
# MySQL configurations
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pancasila_recognition'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)