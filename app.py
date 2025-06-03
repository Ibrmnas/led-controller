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
    try:
        app.run(host='0.0.0.0', port=50100)
    except KeyboardInterrupt:
        print("Shutting down the server...")
    finally:
        cleanup_gpio()  # Ensure GPIO cleanup on server shutdown
