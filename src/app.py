#!/usr/bin/env python
from flask import Flask, url_for
import os

# Shared config variables
IMAGES_DIR = os.path.abspath('data/images')

app = Flask(__name__)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename)
)

from views import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
