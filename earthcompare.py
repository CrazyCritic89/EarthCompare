difRatio = 1/2

mass = float(input("Enter Earth Masses: "))
radius = float(input("Enter Radius: "))
gravity = float(input("Enter Gravity: "))
temp = float(input("Enter Surface Temperatue: "))
pres = float(input("Enter Surface Pressure: "))

atmos1 = float(input("Enter Nitrogen Percentage: "))
atmos2 = float(input("Enter Oxygen Percentage: "))

match int(input("Water[0] or Argon[1]? ")):
    case 0:
        atmos3 = float(input("Enter Water Percentage: "))
        atm3cp = 0.25
    case 1:
        atmos3 = float(input("Enter Argon Percentage: "))
        atm3cp = 0.9

compo1 = float(input("Enter Rock Percentage: "))
compo2 = float(input("Enter Metal Percentage: "))

rotper = float(input("Enter Rotational Period: "))

massDif =   100 - (abs(1 - mass)        / ((1 + mass)        / 2)) * difRatio * 100
radiusDif = 100 - (abs(6378 - radius)   / ((6378 + radius)   / 2)) * difRatio * 100
gravityDif =100 - (abs(9.807 - gravity) / ((9.807 + gravity) / 2)) * difRatio * 100
tempDif =   100 - (abs(288.15 - temp)   / ((288.15 + temp)   / 2)) * difRatio * 100
presDif =   100 - (abs(1 - pres)        / ((1 + pres)        / 2)) * difRatio * 100
atmos1Dif = 100 - (abs(77.9 - atmos1)   / ((77.9 + atmos1)   / 2)) * difRatio * 100
atmos2Dif = 100 - (abs(20.9 - atmos2)   / ((20.9 + atmos2)   / 2)) * difRatio * 100
atmos3Dif = 100 - (abs(atm3cp - atmos3) / ((atm3cp + atmos3) / 2)) * difRatio * 100
compo1Dif = 100 - (abs(70.0 - compo1)   / ((70.0 + compo1)   / 2)) * difRatio * 100
compo2Dif = 100 - (abs(30.0 - compo2)   / ((30.0 + compo2)   / 2)) * difRatio * 100
rotperDif = 100 - (abs(1 - rotper)      / ((1 + rotper)      / 2)) * difRatio * 100

print((massDif+radiusDif+gravityDif+tempDif+presDif+atmos1Dif+atmos2Dif+atmos3Dif+compo1Dif+compo2Dif+rotperDif)/11)