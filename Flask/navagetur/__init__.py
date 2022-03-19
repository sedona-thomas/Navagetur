
import os
from flask import Flask, session, request

app = Flask(__name__)
app.config.from_pyfile('../config.py')

import navagetur.main