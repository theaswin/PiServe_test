'''
This perticular file handles the input sensors
'''
from DBHadler import dbHandlerMaster

class SensorHandlerMaster(dbHandlerMaster):
    def __init__(self) -> None:
        self.DataBaseName = 'SensorData'

    def addNewSenosr(self,table):
        self.table = table
        self.connectWithDataBase()
        self.CreateNewTableForNewSensor(self.table)


