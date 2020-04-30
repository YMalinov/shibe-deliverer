#!/usr/bin/python3

from flask import Flask, request, render_template, abort
import requests

import os

def get_abs_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)

app = Flask(__name__, template_folder=get_abs_path('templates'))

URL = 'http://shibe.online/api/shibes?count=1&httpsUrls=true'

@app.route('/', methods = ['GET'])
def index():
    try:
        count = request.args.get('count', default=1, type=int)
        if count > 100:
            count = 1

        shibes = requests.get(
                f'http://shibe.online/api/shibes?count={count}&httpsUrls=true',
                timeout=5
                ).json()
        return render_template(
                'index.html',
                shibes=shibes
                )
    except Exception as e:
        print(e)
        return abort(500)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
