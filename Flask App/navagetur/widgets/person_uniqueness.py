#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/09/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

from uszipcode import SearchEngine


class RecordingPrivacyFinder(object):
    def __init__(self):
        self.engine = SearchEngine()
        self.state = self.getState()
        self.qualities = {
            "zipcode": None,
            "gender": None,
            "income": None
        }

    def askForQualities(self):
        pass


def test():
    pass


if __name__ == "__main__":
    test()
