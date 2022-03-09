#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

import os
import re
import datetime
from passwords import Password
from JSONDatabase import *


class AccountData(object):

    def __init__(self, filename):
        self.accounts = JSONDatabase(filename)
        self.fields = ["site_name", "username", "password", "password_change",
                       "mfa", "app_passcodes", "authenticators", "keys", "phone_numbers"]

    def getFields(self):
        return self.fields

    def getAccounts(self):
        return self.accounts

    def askForAccounts(self):
        while input("Would you like to enter an account (y/n)?") != "n":
            self.askForAccount()

    def askForAccount(self):
        data = {}
        data["site_name"] = input("Enter site name: ")
        data["username"] = input("Enter username: ")
        data["password"] = input("Enter password: ")
        data["password_change"] = input(
            "Enter date of last password change (MM/DD/YYYY):")
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
        self.accounts.add(data)

    def askLoop(self, prompt):
        li, next = [], input(prompt + " or type \"done\" when finished")
        while next != "done":
            li.append(next)
            next = input(prompt + " or type \"done\" when finished")
        return li

    def getDate(self, date_str):
        date = date_str.strip().split("/")
        return datetime.datetime(int(date[2]), int(date[0]), int(date[1]))

    def dateString(self, date):
        return date.strftime("%x")

    def returnTable(self):
        db, tb = self.accounts.getAll(), "<table id=\"account_data\"> <tr>"
        for field in self.fields:
            tb += "<th>" + field + "</th>"
        tb += "</tr>"
        tb += self.accounts.getTableBody()
        return tb + "</table>"


class AccountSecurity(object):

    def __init__(self, data):
        self.data = data
        self.accounts = self.data.getAccounts()
        self.fields = self.data.getFields()

    def generateStats(self):
        self.passwordStats()

    def passwordStats(self):
        password_handler = Password()
        for row in self.accounts:
            self.fields.append("time_to_crack")
            row["time_to_crack"] = password_handler.brute_force_attack(
                row["password"])

    def returnTable(self):
        tb = "<table id=\"privacy_settings\"> <thead><tr>"
        for field in self.fields:
            tb += "<th>" + field + "</th>"
        tb += "</tr> </thead>"
        tb += "<tbody>" + self.accounts.getTableBody() + "</tbody>"
        return tb + "</table>"

    def makeHtml(self):
        f = open("table.html", "w")
        with open("../pages/page_framework.html") as file:
            li = self.splitOnTag("".join([line for line in file]))
        f.write(li[0] + self.returnTable() + li[1])
        f.close()

    def splitOnTag(self, text):
        open_tag = re.search("<\s*article\s*class=\"content\">", text)
        return [text[:open_tag.span()[-1]], text[open_tag.span()[-1]:]]


def test():
    data = AccountData("../data/test.json")
    data.askForAccounts()
    security = AccountSecurity(data)
    security.generateStats()
    security.makeHtml()


if __name__ == "__main__":
    test()
