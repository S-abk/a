import serial
import time
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')
arduino = serial.Serial('/dev/ttyACM0', 9600)

data_points = []

def read_sensor_data():
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")  # Debugging output
            if "Proximity:" in data:
                proximity = 1 if "Detected" in data else 0
                timestamp = time.time()
                data_points.append((timestamp, proximity))
                if len(data_points) > 100:  # Limit number of points
                    data_points.pop(0)
                socketio.emit('updatePlot', {'timestamp': timestamp, 'proximity': proximity})
        time.sleep(0.1)

def generate_plot():
    times, proximities = zip(*data_points) if data_points else ([], [])
    plt.figure(figsize=(10, 5))
    plt.plot(times, proximities, label='Proximity', color='b')
    plt.xlabel('Time (s)')
    plt.ylabel('Proximity Detected (1/0)')
    plt.title('Real-time Proximity Sensor Data')
    plt.ylim(-0.1, 1.1)  # Keep Y-axis consistent for clarity
    plt.grid(True)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()  # Close the plot to free memory
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return image_base64

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('init', {'image': generate_plot()})

@socketio.on('request_update')
def handle_request_update():
    emit('updatePlot', {'image': generate_plot()})

if __name__ == '__main__':
    sensor_thread = threading.Thread(target=read_sensor_data)
    sensor_thread.daemon = True
    sensor_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
