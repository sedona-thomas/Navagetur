#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"


import datetime
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
