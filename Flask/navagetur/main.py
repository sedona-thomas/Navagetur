from navagetur import app
from flask import render_template, request, redirect
import requests


@app.route("/")
def index():
    return render_template("../../website/pages/index.html")
