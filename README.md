
# Real-Time Proximity Sensor Data Visualization

This project visualizes real-time proximity sensor data using an Arduino, Flask, and Chart.js. It demonstrates how to capture proximity data from a sensor, process it through a Python Flask backend, and dynamically display it on a web interface using Chart.js.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3
- pip
- Flask
- Arduino IDE
- An Arduino-compatible proximity sensor

## Hardware Setup

- **Arduino Board**: Connect the proximity sensor to your Arduino board according to the sensor specifications.
- **Connections**: Ensure the following connections:
  - Sensor output pin to a designated digital pin on the Arduino
  - Sensor power and ground pins to the Arduino power and ground

## Software Setup

### Arduino

1. **Upload Sketch**: Load and upload the provided Arduino sketch to your Arduino board. The sketch is responsible for reading the proximity sensor and sending the data via serial to the connected computer.

### Flask Application

1. **Installation**: Install Flask and necessary libraries:
   ```bash
   pip install Flask flask-socketio eventlet
   ```

2. **Running the Server**:
   ```bash
   python app.py
   ```

   This will start the Flask server on `localhost` on port `5000`.

### Web Interface

Open your browser and navigate to `http://localhost:5000` to view the real-time data visualization.

## Usage

Once everything is set up, move objects near the proximity sensor to see the real-time updates on the web interface. The web page displays a graph that updates every second to reflect the current proximity state detected by the sensor.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
