

# By default, 1 in the dot product = 10mS
def getConductance(v, g1 = 0.00001):
    return v*g1

def getResistance(v, g1 = 0.00001):
    if(v==0):
        return -1
    return round(1.0/getConductance(v, g1),2)

def getG(V, g1=0.00001):
    G = []
    for x in V:
        G.append(getConductance(x, g1))
    return G

def getR(V, g1 = 0.00001):
    R = []
    for x in V:
        R.append(getResistance(x,g1))
    return R

# By default, 1 in the dot product = 1% Duty Cycle
def getDutyCycle(v, dc1 = 0.01):
    return v*dc1

def getDC(V, dc1 = 0.01):
    DC = []
    for x in V:
        DC.append(getDutyCycle(x, dc1))
    return DC

def getV(Ve, VCC = 5, dc1 = 0.01):
    V = []
    for x in Ve:
        V.append(getDutyCycle(x,dc1)*VCC)
    return V
  
def getPulseWidth(v,period = 10e-9, dc1 = 0.01, tr = 25e-12, tf = 25e-12):
    dc = getDutyCycle(v,dc1)
    return (period*dc)-(tr+tf)/2

def getPW(V,period = 10e-9, dc1 = 0.01, tr = 25e-12, tf=25e-12):
    PW = []
    for x in V:
        PW.append(getPulseWidth(x,period,dc1,tr,tf))
    return PW

# By default, the ceiling to ground voltage is 5V at DC
def predictDotProduct(A,B):
    ag = getG(A)
    bv = getV(B)
    total = 0.0
    for i in range(len(ag)):
        total+=ag[i]*bv[i]
    return total


print(getPW([1,2,3,4,5]))
print(getR([1,2,3,4,5]))
print(predictDotProduct([1,2,3,4,5],[1,2,3,4,5]))
print(predictDotProduct([1,2,3,4,5],[1,2,3,4,5])*2000000)