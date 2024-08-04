from flask import Flask, render_template, jsonify
import serial
import time
import threading

app = Flask(__name__)
arduino = serial.Serial('/dev/ttyAMA0', 9600) // Change the port to the one you are using

data_points = []

def read_sensor_data():
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")  # Debugging output
            if "Proximity: Detected" in data:
                proximity = 1
            elif "Proximity: Not Detected" in data:
                proximity = 0
            else:
                continue  # If the data is not relevant, continue without processing
            timestamp = time.time()
            data_points.append((timestamp, proximity))
            if len(data_points) > 100:  # Limit number of points
                data_points.pop(0)
        time.sleep(0.1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Serve the latest 100 data points
    return jsonify(data_points[-100:])

if __name__ == '__main__':
    sensor_thread = threading.Thread(target=read_sensor_data)
    sensor_thread.daemon = True
    sensor_thread.start()
    app.run(host='0.0.0.0', port=5000)
