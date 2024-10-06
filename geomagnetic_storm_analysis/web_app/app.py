
from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='../3d_model', static_url_path='/3d_model')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
