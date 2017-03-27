import sys


try:
    5 / 0
except Exception as e:
    print 'Exception: ', type(e), e

print "but life goes on0"
