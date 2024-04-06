import requests

difRatio = 1/2

system = input("Enter System: ")

ses = requests.Session()

data ={"systemName" : system}

res = ses.get('https://www.edsm.net/api-system-v1/bodies', params=data)
resj = res.json()

tmp = 0
for i in resj["bodies"]:
    if i["subType"] == "Earth-like world":
        print("\033[92m", end="")
        print(i["name"] + " (Earth-like world)" + "\033[0m")
    else:
        print(i["name"])

print("") #Need that new line

body = input("Enter Body / Object: ")

index = -1
tmp = 0
for i in resj["bodies"]:
    if i["name"] == body:
        index = tmp
    if i["name"].find(body) != -1:
        index = tmp
    tmp += 1

if index == -1: #Assume we're meaning to input an object
    pass

#print(resj["bodies"][index])

mass = resj["bodies"][index]["earthMasses"]
radius = resj["bodies"][index]["radius"]
gravity = resj["bodies"][index]["gravity"]
temp = resj["bodies"][index]["surfaceTemperature"]
pres = resj["bodies"][index]["surfacePressure"]

atmos1 = resj["bodies"][index]["atmosphereComposition"]["Nitrogen"]
atmos2 = resj["bodies"][index]["atmosphereComposition"]["Oxygen"]

for i in resj["bodies"][index]["atmosphereComposition"]: #This is awful
    match i:
        case "Water":
            atmos3 = resj["bodies"][index]["atmosphereComposition"]["Water"]
            atm3cp = 0.25
        case "Argon":
            atmos3 = resj["bodies"][index]["atmosphereComposition"]["Argon"]
            atm3cp = 0.9

compo1 = resj["bodies"][index]["solidComposition"]["Rock"]
compo2 = resj["bodies"][index]["solidComposition"]["Metal"]

rotper = resj["bodies"][index]["rotationalPeriod"]

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

print("It is " + str(round(((massDif+radiusDif+gravityDif+tempDif+presDif+atmos1Dif+atmos2Dif+atmos3Dif+compo1Dif+compo2Dif+rotperDif)/11), 2)) + "% like Earth")