#!/usr/bin/env python3

import sys

[domdom, domhet, domrec, hethet, hetrec, recrec] = sys.argv[1:7]

dom_offspring = (
    (int(domdom) * 2) 
    + (int(domhet) * 2)
    + (int(domrec) * 2)
    + (int(hethet) * 2 * 0.75)
    + (int(hetrec) * 2 * 0.5)
    + (int(recrec) * 2 * 0)
    )

print(dom_offspring)