#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2012-2017 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html

# @file    plotXMLAttr.py
# @author  Jakob Erdmann
# @date    2017-12-04
# @version $Id$
"""generate boxplot for an aribitrary xml attribute"""

from __future__ import absolute_import
from __future__ import print_function
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))
from sumolib.output import parse
from sumolib.miscutils import Statistics

def main(xmlfile, tag, attr):
    stats = Statistics('%s %s' % (tag, attr))
    for elem in parse(xmlfile, tag):
        stats.add(float(elem.getAttribute(attr)), elem.id)
    print(stats)
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        sys.exit(e)
    fig = plt.figure()
    plt.ylabel("%s %s" % (tag, attr))
    plt.xlabel(xmlfile)
    plt.boxplot([stats.values])
    plt.legend(loc='best')
    plt.show()


if __name__ == "__main__":
    main(*sys.argv[1:])
