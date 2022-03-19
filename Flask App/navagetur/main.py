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


@app.route("/education.html")
def education():
    return render_template("education.html")


@app.route("/widgets.html")
def widgets():
    return render_template("widgets.html")


@app.route("/password.html")
def password():
    return render_template("password.html")


@app.route("/account_security.html")
def account_security():
    return render_template("account_security.html")


@app.route("/law_locator.html")
def law_locator():
    return render_template("law_locator.html")


@app.route("/personal_uniqueness.html")
def personal_uniqueness():
    return render_template("personal_uniqueness.html")


@app.route("/table.html")
def table():
    return render_template("table.html")


@app.route("/citations.html")
def citations():
    return render_template("citations.html")
