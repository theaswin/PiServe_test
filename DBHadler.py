'''
This perticular file Handle our database functionalities.Such as creating database,
creation of new table for input data,updating data,adding new sensor
'''
import sqlite3
from utils import UtilsMaster
import csv
import pandas as pd
import os

class dbHandlerMaster(UtilsMaster):
    def __init__(self):
        self.newTableForSensor = 'Sensor2'
        self.DataBaseName = 'Sensor'
        self.csvFile = 'PYgenerated/data.csv'
        self.output_csv = 'DBExtracted/output.csv'

    def connectWithDataBase(self):
        try:
            conn  = sqlite3.connect(self.DataBaseName+'.db')
        except ConnectionError:
            raise ConnectionError()
        return conn
        

    def createNewTable(self):
        try:
            conn  = self.connectWithDataBase()
            conn.execute('''
                CREATE TABLE IF NOT EXISTS SensorData (
                         date TEXT,
                         DATA INT
                )
                         ''')
            # conn.execute("Drop table SensorData")
            print("Created")
            conn.commit()
            conn.close()
        except:
            print("failed")


    def insertDataIntoTable(self):
        conn = self.connectWithDataBase()
        
        with open(self.csvFile,'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader,None)
            
            for row in csv_reader:
                conn.execute('''
                INSERT INTO SensorData (DATA,date) VALUES (?,?)
                    ''',(row[0],row[1]))
            conn.commit()
            conn.close()
        



    def ExtractingDataFromDB(self):
        self.fileFromDb = 'DBExtracted/'
        self.fileName = 'output.csv'
        try:
            conn = self.connectWithDataBase()
            sqlSelect = "SELECT *  FROM SensorData"
            cursor = conn.cursor()

            cursor.execute(sqlSelect)

            results = cursor.fetchall()

            #Get the headers of the csv file
            headers = [i[0] for i in cursor.description]

            #Make the CSV ouput directory
            if not os.path.isdir(self.fileFromDb):
                os.makedirs(self.fileFromDb)

            # Open CSV file for writing.
            csvFile = csv.writer(open(self.fileFromDb + self.fileName, 'w', newline=''),delimiter=',', lineterminator='\r\n',quoting=csv.QUOTE_ALL, escapechar='\\')

            # Add the headers and data to the CSV file.
            csvFile.writerow(headers)
            csvFile.writerows(results)


        except Exception as e:
            print("not extracted")
        


    def updateExistingTable(self):
        conn = self.connectWithDataBase()
        cursor = conn.cursor()
        new_date = 88
        data = 4
        cursor.execute('''
            UPDATE SensorData
                SET date = ?
                WHERE DATA = ?
                ''',(new_date,data))
        conn.commit()
        conn.close()

    def CreateNewTableForNewSensor(self):
        conn  = self.connectWithDataBase()
        cursor = conn.cursor()



# v = dbHandlerMaster()
# v.createNewTable()
# v.insertDataIntoTable()
# v.updateExistingTable()
# v.ExtractingDataFromDB()
