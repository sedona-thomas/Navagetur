#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

import json
import datetime
from passwords import Password


class JSONDatabase(object):
    def __init__(self, filename):
        self.filename = filename
        self.database = self.read()

    def add(self, entry):
        self.database.append(entry)
        self.write()

    def getAll(self):
        return self.database

    def read(self):
        with open(self.filename) as file:
            return json.load(file)

    def write(self):
        f = open(self.filename, "w")
        f.write(json.dumps(self.database))
        f.close()

    def getTable(self):
        return "<table>" + self.getTableBody() + "</table>"

    def getTableBody(self):
        tb = ""
        for row in db:
            tb += "<tr>"
            for k in row:
                tb += "<th>" + row[k] + "</th>"
            tb += "</tr>"
        return tb


class AccountData(object):

    def __init__(self, filename):
        self.accounts = JSONDatabase(filename)
        self.fields = ["site_name", "username", "password", "password_change",
                       "mfa", "app_passcodes", "authenticators", "keys", "phone_numbers"]

    def getFieldsDb(self):
        return self.fields, self.accounts

    def getAccounts(self):
        return self.accounts.getAll()

    def askForAccounts(self):
        while input("Would you like to enter an account (y/n)?") != "n":
            self.askForAccount()

    def askForAccount(self):
        data = {}
        data["site_name"] = input("Enter site name: ")
        data["username"] = input("Enter username: ")
        data["password"] = input("Enter password: ")
        data["password_change"] = self.askForDateOfPasswordChange()
        self.multiFactorAuthentication()
        self.accounts.add(data)

    def askLoop(self, prompt):
        li, next = [], input(prompt + " or type \"done\" when finished")
        while next != "done":
            li.append(next)
            next = input(prompt + " or type \"done\" when finished")
        return li

    def multiFactorAuthentication(self):
        data["mfa"] = input("Is multi-factor authentication enabled (y/n): ")
        if data["mfa"] == "y":
            data["app_passcodes"] = input(
                "Have you saved app passcodes (y/n): ")
            data["authenticators"] = self.askLoop("Enter authenticator device")
            data["keys"] = self.askLoop("Enter authenticator key")
            data["phone_numbers"] = self.askLoop("Enter phone number")
        else:
            for k in ["app_passcodes", "authenticators", "keys", "phone_numbers"]:
                data[k] = None

    def askForDateOfPasswordChange(self):
        date_str = input("Enter date of last password change (MM/DD/YYYY):")
        date = date_str.strip().split("/")
        return datetime.datetime(int(date[2]), int(date[0]), int(date[1]))

    def dateString(self, date):
        return date.strftime("%x")

    def returnTable(self):
        db, tb = self.accounts.getAll(), "<table id=\"account_data\"> <tr>"
        for field in self.fields:
            tb += "<th>" + field + "</th>"
        tb += "</tr>"
        self.accounts.getTableBody()
        return tb + "</table>"


class AccountSecurity(object):

    def __init__(self, fields, accounts):
        self.accounts = accounts
        self.fields = fields

    def generateStats(self):
        self.passwordStats()

    def passwordStats(self):
        password_handler = Password()
        for row in db:
            row["time_to_crack"] = password_handler.brute_force_attack(
                row["password"])

    def returnTable(self):
        db, tb = self.accounts.getAll(), "<table id=\"privacy_settings\"> <tr>"
        for field in self.fields:
            tb += "<th>" + field + "</th>"
        tb += "</tr>"
        self.accounts.getTableBody()
        return tb + "</table>"

    def makeHtml(self):
        f = open("table.html", "w")
        f.write(self.returnTable())
        f.close()


def test():
    db = AccountData("../data/test.json")
    db.askForAccounts()
    security = AccountSecurity(getFieldsDb())
    security.generateStats()
    security.makeHtml()


if __name__ == "__main__":
    test()
