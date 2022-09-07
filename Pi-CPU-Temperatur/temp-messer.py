from gpiozero import CPUTemperature
from flask import Flask, render_template

cpu = CPUTemperature()
app = Flask('temp-messer')

@app.route('/')
def index():
    return render_template('index.html', temp=cpu.temperature)

if __name__ == '__main__':
    app.run()
else:
    print('The script wasnt able to start the localhost server to show the CPU temperature.')