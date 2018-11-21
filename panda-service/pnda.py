import os
from os import walk
import random
from flask import Flask, request, render_template, redirect, url_for, flash, make_response, send_from_directory

app = Flask(__name__, static_url_path='')

curr_path = os.path.dirname(os.path.abspath(__file__))

f = []


# @app.route('/')
# def pnda_main():
#     return "PANDA"

def get_random_file():
    for (dirpath, dirnames, filenames) in walk(curr_path + "/resources"):
        f.extend(filenames)
        break
    return random.choice(f)

@app.route('/')
def pnda_main():
    # response = make_response(redirect(url_for('resources')))
    response = make_response(redirect(url_for('send_js', path=get_random_file())))
    return response

@app.route('/resources/<path:path>')
def send_js(path):
    return send_from_directory('resources', path)


if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)))

