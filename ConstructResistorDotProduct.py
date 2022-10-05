from ResistorDotProduct import *

aVector = range(1,257)      # 1,2,...,256
bVector = range(1,17)*16    # 1,2,...,16,1,2,...,16,...

total = 0
for i in range(len(aVector)):
    total+=aVector[i]*bVector[i]
print(total)
    
header = "Header Comment"

PW = getPW(bVector)
R = getR(aVector)

f = open("dotproductNetlist.txt", "w+")

f.write("* "+header+"\n\n")
f.write(".TEMP 25\n.OPTION\n.PARAM\n.GLOBAL gnd!\n\n")
f.write(".param pvcc=5\n.param period=10n\n.param tr=25p\n.param tf=25p\n\n")
f.write("Vgg gnd! 0 DC = 0\n")

for i in range(len(PW)):
    f.write("Vv"+str(i)+" V"+str(i)+" gnd! PULSE (0 pvcc 0 tr tf ")
    f.write("{:e}".format(PW[i]) + " period)\n")

f.write("\n\n")

for j in range(len(R)):
    f.write("RR"+str(j)+" V"+str(j)+" Vout "+"{:e}".format(R[j])+" $[RP]\n")

f.write("\nRRLoad Vout gnd! 0 $[RP]\n\n")
f.write(".tran 1p 100n Start = 0.0\n\n")
f.write(".OP\n")
f.write(".probe tran i(*)\n")
f.write(".probe tran v(*)\n\n")
f.write(".measure tran iout avg i(RRLoad)\n")
f.write(".measure dotProduct PARAM = '2000000*Iout'\n\n")
f.write(".OPTION ACCURATE\n")
f.write(".OPTION POST\n\n")
f.write(".END")

f.close()