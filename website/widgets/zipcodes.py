#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Consent law checker by zipcode
"""

__author__ = "Christian Revels-Robinson"
__authors__ = ["Christian Revels-Robinson", "Sedona Thomas"]
__credits__ = ["Christian Revels-Robinson", "Sedona Thomas"]
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Christian Revels-Robinson"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "crr2159@columbia.edu"

from uszipcode import SearchEngine


class RecordingPrivacyFinder(object):
    # source: https://www.mwl-law.com/wp-content/uploads/2018/02/RECORDING-CONVERSATIONS-CHART.pdf
    def __init__(self):
        self.engine = SearchEngine()
        self.state = self.getState()
        self.one_party = ["AL", "AK", "AR", "AZ", "DC",
                          "GA", "HI", "ID", "IN", "IA", "KS", "KY", "MI",
                          "LA", "ME", "MN", "MS", "MO", "NE",
                          "NJ", "NM", "NY", "NC", "ND",
                          "OH", "OK", "RI", "SC", "SD",
                          "TN", "TX", "UT", "VA", "WV", "WY"]
        self.mixed_party = ["WI", "WA", "PA", "OR", "NV",
                            "NH", "MT", "MA", "MD", "IL",
                            "FL", "DE", "CT", "CO", "CA"]
        self.no_regulation = ["VT"]

    def getState(self):
        val = input("Enter zip code: ")
        zipcode = self.engine.by_zipcode(val)
        return zipcode.state

    def checkLaws(self):
        return self.state in self.one_party or self.state in self.mixed_party

    def printLaws(self):
        if self.state in self.one_party:
            print("Your state has one party consent laws. ")
        elif self.state in self.mixed_party:
            print("Your state has mixed party consent laws.")
        elif self.state in self.no_regulation:
            print("Your state has not regulated consent laws. ")


class DataPrivacyFinder(object):
    # source: https://www.ncsl.org/research/telecommunications-and-information-technology/2021-consumer-data-privacy-legislation.aspx
    def __init__(self):
        self.engine = SearchEngine()
        self.state = self.getState()
        self.regulated = ["AR", "AZ", "CA", "CO", "FL",
                          "MD", "MT", "NV", "OR", "SC", "SD", "UT", "VA"]

    def getState(self):
        val = input("Enter zip code: ")
        zipcode = self.engine.by_zipcode(val)
        return zipcode.state

    def checkLaws(self):
        return self.state in self.regulated

    def printLaws(self):
        if self.state in self.regulated:
            print("Your state has data privacy regstrictions. ")
        else:
            print("Your state does not have data privacy restrictions. ")


def run():
    finder = PrivacyFinder()
    finder.printLaws()


if __name__ == "__main__":
    run()
