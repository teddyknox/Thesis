#!/usr/bin/env python
from flask import Flask, url_for
import os

DEBUG = os.environ.get('DEBUG', 'true') == 'true'
PORT = int(os.environ.get('PORT', '8080'))

app = Flask(__name__)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename)
)

from views import *

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
