#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

from tabnanny import filename_only
from JSONDatabase import *


class HTMLProcesser(object):

    def makeHtml(self, filename, headings, database):
        self.generateStats()
        f = open(filename_only, "w")
        with open("../pages/page_framework.html") as file:
            file_str = "".join([line for line in file])
            li = self.splitOnTag(file_str, "article", tag_class="content")
        f.write(li[0] + self.makeTable(headings, database) + li[1])
        f.close()

    def splitOnTag(self, text, tag, tag_class="", tag_id=""):
        c = "class=\"" + tag_class + "\"" if len(tag_class) > 0 else tag_class
        id = "id=\"" + tag_id + "\"" if len(tag_id) > 0 else tag_id
        expression = "<\s*" + tag + "\s*" + c + "\s*" + id + ">"
        open_tag = re.search(expression, text)
        return [text[:open_tag.span()[-1]], text[open_tag.span()[-1]:]]

    def makeTable(self, headings, database, tag_id=""):
        id = " id=\"" + tag_id + "\"" if len(tag_id) > 0 else ""
        tb = "<table" + id + "> <tr>"
        for heading in headings:
            tb += "<th>" + heading + "</th>"
        tb += "</tr>"
        tb += list.makeTableBody()
        return tb + "</table>"
