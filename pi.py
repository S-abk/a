from flask import Flask, request, render_template, redirect, url_for
import serial

app = Flask(__name__)

arduino = serial.Serial('/dev/ttyACM0', 9600)

def control_led(state):
    if state == 'on':
        arduino.write(b'1')
    elif state == 'off':
        arduino.write(b'0')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led', methods=['POST'])
def led():
    state = request.form.get('state')
    control_led(state)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
