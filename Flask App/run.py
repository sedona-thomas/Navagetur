#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

import sys
from navagetur import app

if __name__ == '__main__':
    port = 5000 if len(sys.argv) == 1 else sys.argv[1]
    local = True
    if local:
        app.run(host="127.0.0.1", port=port, debug=True)
    else:
        app.run(host="0.0.0.0", port=port, debug=True)
