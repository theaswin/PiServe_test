from flask import Flask,render_template,request,send_file

from DBHadler import dbHandlerMaster 
from utils import UtilsMaster
from SensorHandler import SensorHandlerMaster
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from VizHandler import VisualisatioMaster

app = Flask(__name__)

fig,ax = plt.subplots(figsize = (6,6))
ax = sns.set_style(style="darkgrid")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_new_sensor',methods = ['GET'])
def add_new_sensor():
    name = request.args.get('name')
    new_sensor = SensorHandlerMaster()
    new_sensor.addNewSenosr(name)
    return render_template('add_new_sensor.html')


    



@app.route('/register_sensor',methods = ['GET'])
def register_sensor():
    id = request.args.get('id')
    name = request.args.get('name')
    input_nodes = request.args.get('input_nodes')
    establised_year = request.args.get('establised_year')
    failure_percentage = request.args.get('failure_percentage')
    working_capacity = request.args.get('working_capacity')
    response_time = request.args.get('response_time')
    latency = request.args.get('latency')
    current_state = request.args.get('current_state')
    future_scope = request.args.get('future_scope')
    creating_sensor = dbHandlerMaster()
    creating_sensor.DataBaseAndTableForNewSensor()
    creating_sensor.CreateCSVForNewSensor(id=id,name=name,inputs_nodes=input_nodes,
    establised_year=establised_year,failure_percentage=failure_percentage,
    working_capacity=working_capacity,Response_time=response_time,latency=latency,
    current_state=current_state,future_scope=future_scope)
    creating_sensor.InsertCSVDataToDB()
    return render_template('register_new_sensor.html')

@app.route('/Dashboard')
def Dashboard():
    return render_template('Dashboard.html')

@app.route('/pipeline')
def pipeline():
    datagen = UtilsMaster()
    datagen.GenerateRandomDataAndDate()
    datagen.DataToCSV()
    db = dbHandlerMaster()
    db.createNewTable()
    db.insertDataIntoTable()
    plots = VisualisatioMaster()
    plots.LinePlot1()
    plots.LinePlot2()
    plots.Countplot1()
    plots.Countplot2()
    plots.Countplot3()
    plots.Countplot4()
    plots.Countplot5()
    plots.Pie()
    return render_template('Dashboard.html')
    


@app.route('/update',methods = ['GET'])
def update():
    name = request.args.get('name')
    id  = request.args.get('id')
    updater = UtilsMaster()
    updater.UpdateExistingSensorData(name=name,id=id)
    return render_template('update.html')

@app.route('/sorting')
def sorting():
    return render_template('sorting.html')



if __name__ == "__main__":
    app.run(debug=True)