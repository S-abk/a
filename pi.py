import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2)  # Allow time for the Arduino to reset

def control_led(state):
    if state == 'on':
        arduino.write(b'1')
    elif state == 'off':
        arduino.write(b'0')

def read_sensor_data():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').rstrip()
        return data
    return None

while True:
    sensor_data = read_sensor_data()
    if sensor_data:
        print(sensor_data)
    control_led('on')
    time.sleep(1)
    control_led('off')
    time.sleep(1)
