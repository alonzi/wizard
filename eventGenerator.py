# pete alonzi (lpa2a@virginia.edu)
# 2020-07-05
# calculate wizard dps optimization

########

from numpy.random import randint as dX
import pandas as pd
import matplotlib.pyplot as plt

def hit(ac=15,mod=5):
    roll = dX(1,21)
    if roll == 20: return 2
    elif roll+mod >= ac: return 1
    else: return 0
        
def fireBolt(l=2,ac=15,mod=5):
    if dX(1,3) == 2: return 0 # assume fifty/fifty hit rate
    # l is level of spell slot
    if l >= 9: return sum(dX(1,11,4)) 
    elif l >= 6: return sum(dX(1,11,3)) 
    elif l >=  3: return sum(dX(1,11,2)) 
    else: return sum(dX(1,11,1))

def magicMissile(l=2,ac=15,mod=5):
    # ac and mod not used in the function
    # 3 darts each 1d4+1 force damage
    # higher level slots give 1 extra dart per level
    dmg = dX(1,5)+1+dX(1,5)+1
    for i in range(l): dmg += dX(1,5)+1
    return dmg

def scorchingRay(l=2,ac=15,mod=5):
    # 3 rays of fire
    # ranged attack for each --> 2d6 fire damage
    #  higher levels give one extra ray per level
    dmg = 0
    if hit(ac,mod): dmg += sum(dX(1,7,2))
    if hit(ac,mod): dmg += sum(dX(1,7,2))
    for i in range(l): 
            if hit(ac,mod): dmg += sum(dX(1,7,2))
    return dmg

def eventGenerator(n=1000,s=scorchingRay,sl=2,ac=15,mod=5):
    foo = []
    for i in range(n): foo.append(s(sl,ac,mod))
    return foo

mm = eventGenerator(100000,magicMissile,2,15,5)
fb = eventGenerator(100000,fireBolt,2,15,5)
sr = eventGenerator(100000,scorchingRay,2,15,5)

foo = {'FireBolt':fb,'MagicMissile':mm,'ScorchingRay':sr}
df = pd.DataFrame(foo)
print(df.head(5))
#df.MagicMissile.plot.hist()
df.plot.hist()
plt.show()


# exploratory data analysis block - this code is temporary
'''

lv = []
fb = []
mm = []
sr = []

for lvl in range(2,4): #2,10
    # print(lvl,fireBolt(lvl),magicMissile(lvl),scorchingRay(lvl))
    for i in range(100000): #100000 is slow
        lv.append(lvl)
        fb.append(fireBolt(lvl))
        mm.append(magicMissile(lvl))
        sr.append(scorchingRay(lvl))


foo = {'SpellLevel':lv,'FireBolt':fb,'MagicMissile':mm,'ScorchingRay':sr}
df = pd.DataFrame(foo)

print(df.head(5))
df.loc[df['SpellLevel']==3].ScorchingRay.plot.hist()
plt.show()

'''
