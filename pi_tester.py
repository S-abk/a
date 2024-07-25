import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

def control_led(state):
    if state == 'on':
        arduino.write(b'1')
    elif state == 'off':
        arduino.write(b'0')

def read_sensor_data():
    time.sleep(1)
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').rstrip()
        return data
    return "No Data"

if __name__ == "__main__":
    while True:
        print(read_sensor_data())
        time.sleep(2)
