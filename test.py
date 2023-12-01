try:
    import sqlite3
    conn = sqlite3.connect('SENSOR.db')
    cur = conn.cursor()

    
    conn.commit()
    conn.close()
except:
    print("failed")