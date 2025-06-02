# app.py
from flask import Flask, render_template
from piUtils import setLedState, cleanup_gpio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/led/<int:state>", methods=['POST'])
def setLed(state):
    if state == 0:
        setLedState(False)
    elif state == 1:
        setLedState(True)
    else:
        return ('Unknown LED state', 400)
    return ('', 204)

if __name__ == '__main__':
    app.run()
