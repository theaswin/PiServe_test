import sqlite3
conn = sqlite3.connect('SensorData.db')
cur = conn.cursor()

cur.execute("delete from DataFromSensor")
conn.commit()
conn.close()