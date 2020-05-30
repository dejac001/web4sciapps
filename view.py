import sys
import compute

def get_input():
    r = float(sys.argv[1])
    return r

def present_output(r):
    s = compute.compute(r)
    print('Hello World! sin(%g)=%g' % (r, s))