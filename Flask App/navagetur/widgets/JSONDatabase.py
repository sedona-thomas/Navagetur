#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"


import json
import os
from navagetur.widgets.encryption import *


class JSONDatabase(object):
    def __init__(self, filename):
        self._filename = filename
        self._database = self.read()

    def __iter__(self):
        ''' Returns the Iterator object '''
        return JSONDatabaseIterator(self)

    def add(self, entry):
        self._database.append(entry)
        self.write()

    def getAll(self):
        return self._database

    def read(self):
        if os.stat(self._filename).st_size == 0:
            return []
        elif self.is_json():
            with open(self._filename) as file:
                return json.load(file)
        else:
            return []

    def write(self):
        with open(self._filename, "w") as f:
            f.write(json.dumps(self._database))

    def getTable(self):
        return "<table>" + self.getTableBody() + "</table>"

    def getTableBody(self):
        tb = ""
        for row in self._database:
            tb += "<tr>"
            for k in row:
                cell = str(row[k]) if type(
                    row[k]) is not list else ", ".join(row[k])
                tb += "<td>" + cell + "</td>"
            tb += "</tr>"
        return tb

    def is_json(self):
        try:
            data = json.load(open(self._filename))
            return True
        except:
            return False


class JSONDatabaseIterator:
    ''' Iterator class '''

    def __init__(self, database):
        self._database = database
        self._index = 0

    def __next__(self):
        ''''Returns the next value from database object's list'''
        if self._index < (len(self._database._database)):
            result = self._database._database[self._index]
            self._index += 1
            return result
        raise StopIteration
