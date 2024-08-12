from flask import Flask, render_template
import time
import math
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    now = time.localtime()
    time_data = {
        'hour': now.tm_hour,
        'minute': now.tm_min,
        'second': now.tm_sec
    }
    return json.dumps(time_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

