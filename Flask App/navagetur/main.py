#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

from navagetur import app
from flask import render_template, request, redirect
import requests


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/widgets.html")
def widgets():
    return render_template("widgets.html")

