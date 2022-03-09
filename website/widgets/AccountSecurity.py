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
from JSONDatabase import *
from AccountData import *


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
        self.generateStats()
        f = open("../pages/table.html", "w")
        with open("../pages/page_framework.html") as file:
            li = self.splitOnContentTag("".join([line for line in file]))
        f.write(li[0])
        f.write("<section id=\"home\" role=\"main\">")
        f.write("<h1> Account Security </h1>")
        f.write("</section>")
        f.write("<section>" + self.returnTable() + "</section>")
        f.write(li[1])
        f.close()

    def splitOnContentTag(self, text):
        open_tag = re.search("<\s*article\s*class=\"content\">", text)
        return [text[:open_tag.span()[-1]], text[open_tag.span()[-1]:]]
