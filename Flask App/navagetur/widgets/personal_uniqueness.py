#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/09/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode


class Uniqueness(object):
    def __init__(self, data):
        self.engine = SearchEngine(simple_or_comprehensive=SearchEngine.SimpleOrComprehensiveArgEnum.comprehensive)
        self.engineSimple = SearchEngine()
        self.data = data
        self.characteristics = ["zipcode", "gender", "income"]

    def personalUniqueness(self):
        s = "<p>There are over 300 million people in the US. Here is how you compare to 2010 Census data.</p>"
        s += "<table>" 
        s += self.returnTable(self.processData())
        s += "</table>"
        return s

    def returnTable(self, demographic_dict):
        tb = "<table id=\"demographic_info\"> <tr>"
        for s in ["Characteristic", "Number of People", "Percent of Population"]:
            tb += "<th>" + s + "</th>"
        tb += "</tr>"
        for s in self.characteristics:
            tb += "<td>{}</td>".format(s.title())
            tb += "<td>{}</td>".format(demographic_dict[s])
            tb += "<td>{:.3g}%</td>".format((demographic_dict[s] / demographic_dict["zipcode"]) * 100)
            tb += "</tr>"
        return tb + "</table>"

    def processData(self):
        zipcode_information = self.engine.by_zipcode(self.data["zipcode"]).to_dict()
        full_dict = {"zipcode": zipcode_information["population"]}

        if self.data["gender"] in ["woman", "man"]:
            gender = 1 if self.data["gender"] == "woman" else 0
            gender_info = zipcode_information["population_by_gender"][0]["values"]
            full_dict["gender"] = gender_info[gender]["y"]
        else:
            full_dict["gender"] = None

        if self.data["income"]:
            income_ranges = {"< $10,000": [0, 10000], 
                             "$10,000-$19,999": [10000, 19999],
                             "$20,000-$29,999": [20000, 29999],
                             "$30,000-$39,999": [30000, 39999], 
                             "$40,000-$49,999": [40000, 49999],
                             "$50,000-$64,999": [50000, 64999],
                             "$65,000-$74,999": [65000, 74999],
                             "$75,000-$99,999": [75000, 99999],
                             "$100,000+": [100000, float("inf")]}
            income = "$100,000+"
            for k in list(income_ranges.keys())[:-1]:
                if income_ranges[k][0] <= self.data["income"] < income_ranges[k][1]:
                    income = k
            income_bracket = list(income_ranges.keys()).index(income)
            income_info = zipcode_information["annual_individual_earnings"][0]["values"]
            full_dict["income"] = income_info[income_bracket]["y"]
        else:
            full_dict["income"] = None

        # if self.data["race"]:
        #     race_categories = ["White", "Black Or African American", "American Indian Or Alaskan Native", "Asian", "Native Hawaiian & Other Pacific Islander", "Other Race", "Two Or More Races"]
        #     full_dict["race"] = None
        # else:
        #     full_dict["race"] = None

        return full_dict


def test():
    data = {"zipcode": 92157,
            "gender": "man",
            "income": 100000}
    uniqueness_processor = Uniqueness(data)
    print(uniqueness_processor.personalUniqueness())


if __name__ == "__main__":
    test()