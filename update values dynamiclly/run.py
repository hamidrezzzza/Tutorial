from flask import Flask, render_template, request, Response
import datetime
import random
import json
import time

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def stuff():
    def get_soc():
        while True:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            temp = random.randint(30,40)
            json_data = json.dumps(
                {'time': time_now, 'value': temp})
            yield f"data:{json_data}\n\n"
            time.sleep(1)
    return Response(get_soc(), mimetype='text/event-stream')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
