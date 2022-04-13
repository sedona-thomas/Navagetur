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
from navagetur.widgets.EncryptedJSONDatabase import *
from navagetur.widgets.AccountData import *
from navagetur.widgets.AccountSecurity import *
from navagetur.widgets.passwords import *
from navagetur.widgets.law_locator import *
from navagetur.widgets.personal_uniqueness import *
from navagetur.widgets.directory_location import *

user_json_filepath = pwd + "navagetur/data/"
user_json_file = "user.json"

is_password = False
current_user_password = ""


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


@app.route('/enter_password', methods=['POST'])
def enter_password():
    password_handler = Password()
    time_to_crack = password_handler.brute_force_attack(
        request.form["password"])
    return render_template("password.html", time_to_crack=time_to_crack)


@app.route('/generate_password', methods=['POST'])
def generate_password():
    password_handler = Password()
    random_password = password_handler.generate(15)
    return render_template("password.html", random_password=random_password)


#############################################################################################

@app.route("/account_security.html")
def account_security():
    if is_password:
        database = EncryptedJSONDatabase(
            user_json_filepath, user_json_file, current_user_password)
        data = AccountData(database)
        security = AccountSecurity(data)
        table = "" if current_user_password == "" else security.returnTable()
        return render_template("account_security.html", table=table)
    else:
        return render_template("account_security.html")


@app.route('/user_password', methods=['POST'])
def user_password():
    global current_user_password
    current_user_password = request.form["password"]
    global is_password
    is_password = True
    return redirect("/account_security.html", code=302)


@app.route('/add_account', methods=['POST'])
def add_account():
    if is_password:
        database = EncryptedJSONDatabase(user_json_file, current_user_password)
        data = AccountData(database)
        data.add(getFields(request))
        security = AccountSecurity(data)
        security.generateStats()
        table = security.returnTable()
        print(database.getAll())
    else:
        table = ""
    return redirect("/account_security.html", code=302)


def getFields(request):
    fields = {"site_name": request.form["site_name"],
              "username": request.form["username"],
              "email": request.form["email"],
              "password": request.form["password"],
              "password_change": dateFormatting(request, "password_change"),
              "mfa": request.form.get("mfa") != None}
    if fields["mfa"]:
        fields["app_passcodes"] = request.form.get("app_passcodes") != None
        fields["authenticators"] = split_list(request.form["authenticators"])
        fields["keys"] = split_list(request.form["keys"])
        fields["phone_numbers"] = split_list(request.form["phone_numbers"])
    else:
        for k in ["app_passcodes", "authenticators", "keys", "phone_numbers"]:
            fields[k] = None
    return fields


def split_list(li):
    return [x.strip() for x in li.split(",")]


def dateFormatting(request, name):
    return request.form["password_change"] if request.form["password_change"] else None

#############################################################################################


@app.route("/law_locator.html")
def law_locator():
    return render_template("law_locator.html")


@app.route('/enter_zipcode', methods=['POST'])
def enter_zipcode():
    zipcode = request.form["zipcode"]
    finder_record = RecordingPrivacyFinder(zipcode)
    finder_data = DataPrivacyFinder(zipcode)
    return render_template("law_locator.html", zipcode=zipcode, record=finder_record.returnLaws(), data=finder_data.returnLaws())


@app.route("/personal_uniqueness.html")
def personal_uniqueness():
    return render_template("personal_uniqueness.html")


@app.route('/enter_characteristics', methods=['POST'])
def enter_characteristics():
    data = {"zipcode": int(request.form["zipcode"]) if len(request.form["zipcode"]) == 5 else None,
            "gender": request.form["gender"] if request.form["gender"] != "choose" else None,
            "income": int(request.form["income"]) if len(request.form["income"]) > 0 else None}
    uniqueness_processor = Uniqueness(data)
    uniqueness = uniqueness_processor.personalUniqueness()
    #uniqueness = ", ".join([str(x) for x in [zipcode, gender, income]])
    return render_template("personal_uniqueness.html", uniqueness=uniqueness)


@app.route("/table.html")
def table():
    return render_template("table.html")


@app.route("/citations.html")
def citations():
    return render_template("citations.html")


# @app.route("/set_password.html")
# def set_password():
#     return render_template("set_password.html")


# @app.route('/set_password', methods=['POST'])
# def save_set_password():
#     global current_user_password
#     current_user_password = request.form["password"]
#     database = EncryptedJSONDatabase(user_json_file, current_user_password)
#     return redirect("/account_security.html", code=302)

# @app.route("/account_security.html")
# def account_security():
#     if is_password:
#         database = EncryptedJSONDatabase(user_json_file, current_user_password)
#         data = AccountData(database)
#         security = AccountSecurity(data)
#         table = "" if current_user_password == "" else security.returnTable()
#         return render_template("account_security.html", table=table)
#     else:
#         return render_template("account_security.html", table="")


# @app.route('/user_password', methods=['POST'])
# def user_password():
#     global current_user_password
#     current_user_password = request.form["password"]
#     global is_password
#     is_password = True
#     return redirect("/account_security.html", code=302)


# @app.route('/add_account', methods=['POST'])
# def add_account():
#     if is_password:
#         database = EncryptedJSONDatabase(user_json_file, current_user_password)
#         data = AccountData(database)
#         data.add(getFields(request))
#         security = AccountSecurity(data)
#         security.generateStats()
#         table = security.returnTable()
#     else:
#         table = ""
#     return redirect("/account_security.html", code=302)


# def getFields(request):
#     fields = {"site_name": request.form["site_name"],
#               "username": request.form["username"],
#               "email": request.form["email"],
#               "password": request.form["password"],
#               "password_change": dateFormatting(request, "password_change"),
#               "mfa": request.form.get("mfa") != None}
#     if fields["mfa"]:
#         fields["app_passcodes"] = request.form.get("app_passcodes") != None
#         fields["authenticators"] = split_list(request.form["authenticators"])
#         fields["keys"] = split_list(request.form["keys"])
#         fields["phone_numbers"] = split_list(request.form["phone_numbers"])
#     else:
#         for k in ["app_passcodes", "authenticators", "keys", "phone_numbers"]:
#             fields[k] = None
#     return fields


# def split_list(li):
#     return [x.strip() for x in li.split(",")]


# def dateFormatting(request, name):
#     return request.form["password_change"] if request.form["password_change"] else None
