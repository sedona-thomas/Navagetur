#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/09/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

from uszipcode import SearchEngine


class Uniqueness(object):
    def __init__(self, data):
        self.engine = SearchEngine()
        self.data = data
        self.characteristics = ["zipcode", "gender", "income"]


def test():
    data = {"zipcode": 92157,
            "gender": "man",
            "income": 100000}
    uniqueness_processor = Uniqueness(data)
    print(uniqueness_processor.personal_uniqueness())


if __name__ == "__main__":
    test()
