'''
Utility file
'''
import random
from datetime import datetime
import csv

class UtilsMaster():
    def __init__(self) -> None:
        self.dataset = []
        self.dates = []
        self.current_datetime = datetime.now()

    def GenerateRandomDataAndDate(self):
        for i in range(1,10):
            self.formatted_datetime = self.current_datetime.strftime("%Y-%m-%d")
            self.randomData = random.randint(0,9)
            self.dataset.append(self.randomData)
            self.dates.append(self.formatted_datetime)
    
    def DataToCSV(self):
        rows = zip(self.dataset,self.dates)
        with open('PYgenerated/data.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['DATA', 'date'])
            csv_writer.writerows(rows)
    

    def GetManualInput(self):
        pass
    
    def EvidentlyDashBoardView(self):
        pass

    def ManualDashboardView(self):
        pass

    def UpdateExistingSensorData(self):
        pass


v = UtilsMaster()
v.GenerateRandomDataAndDate()
v.DataToCSV()