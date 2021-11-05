import glob
import os

from flask import Flask
import json

app = Flask(__name__)


@app.route('/getPhoto')
def get_photo():
    coat_path = './coat'
    trousers_path = './trousers'
    coat_img = glob.glob(os.path.join(coat_path, '*.jpeg'))
    coat_img = coat_img + glob.glob(os.path.join(trousers_path, '*.jpeg'))
    response = app.make_response(json.dumps(coat_img))
    response.access_control_allow_origin = "*"
    return response


if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('127.0.0.1', 8081), app)
    # server.serve_forever()
    app.run(host='127.0.0.1', port=8081, debug=False)
