#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

import re
from passwords import Password
from AccountData import *


class AccountSecurity(object):

    def __init__(self, data):
        self.data = data
        self.accounts = self.data.getAccounts()
        self.fields = self.data.getFields()

    def generateStats(self):
        self.passwordStats()
        self.scoreSafety()

    def passwordStats(self):
        password_handler = Password()
        for row in self.accounts:
            self.fields["time_to_brute_force"] = "Time to Brute Force Attack"
            row["time_to_brute_force"] = password_handler.brute_force_attack(
                row["password"])

    def scoreSafety(self):
        password_handler = Password()
        for row in self.accounts:
            self.fields["safety_score"] = "Safety Score"
            brute_force = password_handler.brute_force_attack_value(
                row["password"])
            pw_change = self.getDate(row["password_change"])
            score = 0
            score += 1 if brute_force / ((60 * 60 * 24 * 365)) > 100 else 0
            score += 1 if self.passwordChange(pw_change) else 0
            score += 1 if row["mfa"] else 0
            row["safety_score"] = str(int((score / 3) * 100)) + "%"

    def returnTable(self):
        tb = "<table id=\"privacy_settings\"> <thead><tr>"
        for field in self.fields.values():
            tb += "<th>" + field + "</th>"
        tb += "</tr> </thead>"
        tb += "<tbody>" + self.accounts.getTableBody() + "</tbody>"
        return tb + "</table>"

    def makeHtml(self):
        self.generateStats()
        f = open("../templates/table.html", "w")
        with open("../templates/page_framework.html") as file:
            li = self.splitOnContentTag("".join([line for line in file]))
        f.write(li[0])
        self.writeBody(f)
        f.write(li[1])
        f.close()

    def writeBody(self, f):
        f.write("<section id=\"home\" role=\"main\">")
        f.write("<h1> Account Security </h1>")
        f.write("<p>Learn more about account security in the education page!</p>")
        f.write("</section>")
        f.write("<section><div class=\"table_wrapper\">")
        f.write(self.returnTable() + "</div></section>")

    def splitOnContentTag(self, text):
        open_tag = re.search("<\s*article\s*class=\"content\">", text)
        return [text[:open_tag.span()[-1]], text[open_tag.span()[-1]:]]

    def passwordChange(self, date):
        '''Checks if password has been changed within six months'''
        if not date:
            return False
        else:
            return (datetime.datetime.now() - date).days > 365 / 2

    def getDate(self, date_str):
        try:
            date = date_str.strip().split("/")
            return datetime.datetime(int(date[2]), int(date[0]), int(date[1]))
        except:
            return None

    def dateString(self, date):
        return date.strftime("%x")
