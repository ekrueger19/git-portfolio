# a = 4 because each square in the grid has 4 sides
a = 4
print a
# this is because the grid is 20x20
b = 20 * 20
print b
# this is to find the number of sides of squares
c = b * a
print c
# this is to find the outer perimeter
g = 20 + 20 + 20 + 20
print g
# this is to set up so that we're only looking at the inner sides of squares
d = c - g
print d
# this is because the squares share sides, so we're not counting stuff twice
e = d / 2
print e
# this is to add back in the outer perimeter
f = e + g
print f
# this is because there isn't an answer for every side
h = f / 2
print h

print '-' * 10
print ((((20 * 20 * 4) - (4 * 20)) / 2) + (4 * 20)) / 2
