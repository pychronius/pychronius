from datetime import *
from cronparser import CronParser

def benchmark_basic_cronparser():
    import time

    rules = [("open", "* 7-19 * * * *"), ("closed", "* 0-6 * * * *"), ("closed", "* 20-23 * * * *")]
    exceptions = [("closed", "* 0-8 * * 6-7 *"), ("closed", "* 17-23 * * 6-7 *"), ("closed", "* * 25 12 * *"), ("closed", "* * 4 7 * *")]

    #Add Holidays
    for d in xrange(1,31, 2):
        for m in xrange(1,12):
            for y in xrange(2000,2020):
                exceptions.append(("closed", "* * %s %s * %s" % (d,m,y)))

    print "Rules: {}".format(len(exceptions)+len(rules))
    start = time.time()
    
    cp = CronParser(rules, exceptions)

    print "Time to build CronParser: {:>19f}s".format(time.time() - start)
    
    start = time.time()
    i = 0
    for y in xrange(2014,2015):
        for m in xrange(1,13):
            for d in xrange(1,28):
                for h in xrange(0,24):
                        i+=1
                        day = datetime(y,m,d,h,0)

    delta_dtos = time.time() - start
    print "Time to build {} datetime objects: {:f}s".format(i, delta_dtos)


    start = time.time()
    i = 0
    for y in xrange(2014,2015):
        for m in xrange(1,13):
            for d in xrange(1,28):
                for h in xrange(0,24):
                        i+=1
                        cp.pick_rules(datetime(y,m,d,h,0))

    delta_pick_rules = time.time() - start
    print "Time to run {} rule checks: {:>15f}s".format(i, delta_pick_rules)
    print "Difference: {:>33f}s".format(delta_pick_rules - delta_dtos)


if __name__ == "__main__":
    benchmark_basic_cronparser()