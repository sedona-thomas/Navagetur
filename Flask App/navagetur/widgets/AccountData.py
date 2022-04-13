#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"


import datetime
from navagetur.widgets.JSONDatabase import *


class AccountData(object):

    def __init__(self, filename, password=""):
        if password == "":
            self.accounts = JSONDatabase(filename)
        else:
            self.accounts = JSONDatabase(filename, password)
        self.fields = {"site_name": "Website Name",
                       "username": "Username",
                       "email": "Email",
                       "password": "Password",
                       "password_change": "Date of Last Password Change",
                       "mfa": "Multi-Factor Authentication",
                       "app_passcodes": "Generated App Passcodes",
                       "authenticators": "Authenticator Devices",
                       "keys": "Authentication Keys",
                       "phone_numbers": "Phone Numbers"
                       }

    def add(self, field_dict):
        self.accounts.add(field_dict)

    def getFields(self):
        return self.fields

    def getAccounts(self):
        return self.accounts

    def askForAccounts(self):
        while input("Would you like to enter an account (y/n)? ") != "n":
            self.askForAccount()

    def askForAccount(self):
        data = {}
        print("Hit return at any time to skip a field.")
        data["site_name"] = self.processInput("Enter site name: ")
        data["username"] = self.processInput("Enter username: ")
        data["email"] = self.processInput("Enter email: ")
        data["password"] = self.processInput("Enter password: ")
        data["password_change"] = self.processInput(
            "Enter date of last password change (MM/DD/YYYY): ")
        data["mfa"] = self.yes_no_input(
            "Is multi-factor authentication enabled (y/n): ")
        if data["mfa"]:
            data["app_passcodes"] = self.yes_no_input(
                "Have you saved app passcodes (y/n): ")
            data["authenticators"] = self.askLoop(
                "Enter authenticator device: ")
            data["keys"] = self.askLoop("Enter authenticator key: ")
            data["phone_numbers"] = self.askLoop("Enter phone number: ")
        else:
            for k in ["app_passcodes", "authenticators", "keys", "phone_numbers"]:
                data[k] = None
        self.accounts.add(data)

    def processInput(self, prompt):
        user_input = input(prompt)
        return user_input if len(user_input) > 0 else None

    def askLoop(self, prompt):
        li, next = [], self.processInput(
            prompt + " or hit return key when finished: ")
        while next:
            li.append(next)
            next = self.processInput(
                prompt + " or hit return key when finished: ")
        return li

    def yes_no_input(self, prompt):
        user_input = input(prompt)
        return input(prompt) == "y" if len(user_input) > 0 else None

    def returnTable(self):
        db, tb = self.accounts.getAll(), "<table id=\"account_data\"> <tr>"
        for field in self.fields.values():
            tb += "<th>" + field + "</th>"
        tb += "</tr>"
        tb += self.accounts.getTableBody()
        return tb + "</table>"

    def getDate(self, date_str):
        date = date_str.strip().split("/")
        return datetime.datetime(int(date[2]), int(date[0]), int(date[1]))

    def dateString(self, date):
        return date.strftime("%x")
