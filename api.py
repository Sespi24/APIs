x = 0
y = -1
Dx = 0.01

def givenFunction(x,y):
    return ((x+y)/(x-y))

while y < 0:
    print( '(' , ("%.2f" % x) , ',' , ("%.2f" % y) , ')' )
    y = y + Dx*givenFunction(x, y)
    x = x + Dx
