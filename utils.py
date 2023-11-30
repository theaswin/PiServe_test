'''
Utility file
'''
import random
from datetime import datetime
import csv
import sqlite3

class UtilsMaster():
    def __init__(self) -> None:
        self.dates = []
        self.current_datetime = datetime.now()
        self.DataBaseName = 'SENSOR'
        self.response1 ,self.response2,self.response3,self.response4,self.response5= [],[],[],[],[]


    def GenerateRandomDataAndDate(self):
        for i in range(1,900):
            self.formatted_datetime = self.current_datetime.strftime("%Y-%m-%d")
            self.res1 = random.randint(1,20)
            self.res2 = random.randint(1,20)
            self.res3 = random.randint(1,20)
            self.res4 = random.randint(1,20)
            self.res5 = random.randint(1,20)


            self.dates.append(self.formatted_datetime)
            self.response1.append(self.res1)
            self.response2.append(self.res2)
            self.response3.append(self.res3)
            self.response4.append(self.res4)
            self.response5.append(self.res5)
    
    def DataToCSV(self):
        rows = zip(self.response1,self.response2,self.response3,self.response4,self.response5,self.dates)
        with open('PYgenerated/data.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Response1','Response2','Response3','Response4','Response5', 'Date'])
            csv_writer.writerows(rows)
    

    def UpdateExistingSensorData(self,name,id):
        try:
            conn  = sqlite3.connect(self.DataBaseName+'.db')
        
            cursor = conn.cursor()
            self.name = name
            self.id = id
            cursor.execute('''
                UPDATE ActiveSensors
                    SET name = ?
                    WHERE id = ?
                    ''',(self.name,self.id))
            conn.commit()
            conn.close()
        except:
            print("not")
