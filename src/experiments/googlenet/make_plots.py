#!/usr/bin/env python
import sys
import inspect
from os import path as p
from operator import itemgetter as get

wd = p.abspath(p.dirname(inspect.getfile(inspect.currentframe())))

if __name__ == "__main__":
    assert len(sys.argv) > 0
    files = sys.argv[1:]
    logfiles = files[:len(files)/2]
    priorfiles = files[len(files)/2:]
    vals = []
    vals_above_priors = []
    for x, (lf, pf) in enumerate(zip(logfiles, priorfiles)):
        with open(p.join(wd, lf)) as log, open(p.join(wd, pf)) as priors:
            rows = list(log)
            prior = float(list(priors)[1][9:])
            print prior
            idx, val = max(enumerate([float(r.split()[3]) for r in rows[1:]]), key=get(1))
            print "Max accuracy for {}:\n\titeration: {}\n\tmax: {}\n\tprior: {}\n\tdiff: {}".format(lf, rows[idx+1].split()[0], val, prior, val - prior)
            vals.append(val)
            vals_above_priors.append(val - prior)
    avg = float(sum(vals))/len(vals)
    avg_above_priors = float(sum(vals_above_priors))/len(vals_above_priors)
    print "Avg accuracy: {}".format(avg)
    print "Avg accuracy above priors: {}".format(avg_above_priors)
