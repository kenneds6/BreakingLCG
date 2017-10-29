from fractions import gcd

def detriment(i, j, X):
    a1 = X[i] - X[0]
    b1 = X[i+1] - X[1]
    a2 = X[j] - X[0]
    b2 = X[j+1] - X[1]

    det = a1*b2 - a2*b1
    return abs(det)


xVal = [56687054115473550533, 71501923691929981066, 1162551557687152936, 88117163952857350660, 16754986973331962115]


detList = [detriment(1,2,xVal), detriment(2,3,xVal)]

mVal = reduce(gcd, detList)

print "M is " + str(mVal)