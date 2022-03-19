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
    data = AccountData("../data/user.json")
    security = AccountSecurity(data)
    table = security.returnTable()
    return render_template("account_security.html", table=table)


@app.route('/add_account', methods=['POST'])
def add_account():
    fields = {"site_name": request.form["site_name"],
              "username": request.form["username"],
              "password": request.form["password"],
              "password_change": request.form["password_change"],
              "mfa": request.form["mfa"],
              "app_passcodes": split_list(request.form["app_passcodes"]),
              "authenticators": split_list(request.form["authenticators"]),
              "keys": split_list(request.form["keys"]),
              "phone_numbers": split_list(request.form["phone_numbers"])}
    data = AccountData("../data/user.json")
    data.add(fields)
    security = AccountSecurity(data)
    table = security.returnTable()
    return render_template("account_security.html", table=table)


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


def split_list(li):
    return [x.strip() for x in li.split(",")]
