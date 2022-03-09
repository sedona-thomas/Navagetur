#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Consent law checker by zipcode
"""

__author__ = "Christian Revels-Robinson"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Christian Revels-Robinson"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "crr2159@columbia.edu"

from uszipcode import SearchEngine
engine = SearchEngine()
val = input("Enter zip code: ")
zipcode = engine.by_zipcode(val)
state = zipcode.state
one_party = ["AL", "AK", "AR", "AZ", "DC",
             "GA", "HI", "ID", "IN", "IA", "KS", "KY", "MI",
             "LA", "ME", "MN", "MS", "MO", "NE",
             "NJ", "NM", "NY", "NC", "ND",
             "OH", "OK", "RI", "SC", "SD",
             "TN", "TX", "UT", "VA", "WV", "WY"]
mixed_party = ["WI", "WA", "PA", "OR", "NV",
               "NH", "MT", "MA", "MD", "IL",
               "FL", "DE", "CT", "CO", "CA"]
no_regulation = ["VT"]
if state in one_party:
    print("Your state has one party consent laws. ")
if state in mixed_party:
    print("Your state has mixed party consent laws.")
if state in no_regulation:
    print("Your state has not regulated consent laws. ")
