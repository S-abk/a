from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import serial
import time
import threading
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
socketio = SocketIO(app)
arduino = serial.Serial('/dev/ttyACM0', 9600)

data_points = []

def read_sensor_data():
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').rstrip()
            if "Proximity:" in data:
                proximity = 1 if "Detected" in data else 0
                timestamp = time.time()
                data_points.append((timestamp, proximity))
                socketio.emit('updatePlot', {'timestamp': timestamp, 'proximity': proximity})
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    times, proximities = zip(*data_points) if data_points else ([], [])
    plt.figure()
    plt.plot(times, proximities, label='Proximity')
    plt.xlabel('Time (s)')
    plt.ylabel('Proximity')
    plt.title('Real-time Proximity Sensor Data')
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return f'<img src="data:image/png;base64,{image_base64}"/>'

@socketio.on('connect')
def handle_connect():
    emit('init', data_points)

if __name__ == '__main__':
    sensor_thread = threading.Thread(target=read_sensor_data)
    sensor_thread.daemon = True
    sensor_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
