import my_app.views
import os
from flask import Flask, session, request

app = Flask(__name__)

# load main config
app.config.from_pyfile('../config.py')


'''
from flask import Flask, session, request
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from threading import Timer
import sys
# Start using all the regular flask logic
flask_app = Flask(__name__)
# Write to main page

# load main config
flask_app.config.from_pyfile('../config.py')


@flask_app.route("/")
def hello():
    return "Hello World"
# Define function for QtWebEngine


def ui(location):
    qt_app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setWindowTitle("Window Name")
    web.resize(900, 800)
    web.setZoomFactor(1.5)
    web.load(QUrl(location))
    web.show()
    sys.exit(qt_app.exec_())


if __name__ == "__main__":
    # start sub-thread to open the browser.
    Timer(1, lambda: ui("http://127.0.0.1:5000/")).start()
    flask_app.run(debug=False)
'''
