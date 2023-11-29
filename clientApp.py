from flask import Flask,render_template,request

from DBHadler import dbHandlerMaster 
from utils import UtilsMaster
from SensorHandler import SensorHandlerMaster

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def Dashboard():
    return render_template('charts.html')



@app.route('/sorting')
def sorting():
    return render_template('sorting.html')



@app.route('/filtering')
def filtering():
    return render_template('filtering.html')


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


# @app.route('/generateData')
# def generateData():
#     data = UtilsMaster()
#     data.GenerateRandomDataAndDate()
#     data.DataToCSV()
#     db = dbHandlerMaster()
#     db.insertDataIntoTable()
#     return render_template('generate_random_data.html')

if __name__ == "__main__":
    app.run(debug=True)