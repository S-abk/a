import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

def control_led(state):
    if state == 'on':
        arduino.write(b'1')
    elif state == 'off':
        arduino.write(b'0')

# Test the function
control_led('on')
control_led('off')
