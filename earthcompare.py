import requests

difRatio = 1/2

system = input("Enter System: ")

ses = requests.Session()

data ={"systemName" : system}

res = ses.get('https://www.edsm.net/api-system-v1/bodies', params=data)
resj = res.json()

if len(resj) == 0:
    print("Received empty response. System", '"'+system+'"', "may be invalid.")
    sys.exit(0)

tmp = 0
for i in resj["bodies"]:
    if i["subType"] == "Earth-like world":
        print("\033[92m", end="")
        print(i["name"] + " (Earth-like world)" + "\033[0m")
    else:
        print(i["name"] + " (" + i["subType"] + ")")

print("") #Need that new line

body = input("Enter Body / Object: ")

index = -1
tmp = 0
for i in resj["bodies"]:
    if i["name"] == body:
        index = tmp
    if i["name"].find(body) != -1: #Check if we're specifing object in system
        index = tmp
    tmp += 1



mass = resj["bodies"][index]["earthMasses"]
radius = resj["bodies"][index]["radius"]
gravity = resj["bodies"][index]["gravity"]
temp = resj["bodies"][index]["surfaceTemperature"]
pres = resj["bodies"][index]["surfacePressure"]

atmos = []
atmcp = []

for i in resj["bodies"][index]["atmosphereComposition"]: #This is awful
    match i:
        case "Nitrogen":
            atmos.append(resj["bodies"][index]["atmosphereComposition"][i])
            atmcp.append(77.89)
        case "Oxygen":
            atmos.append(resj["bodies"][index]["atmosphereComposition"][i])
            atmcp.append(20.89)
        case "Water":
            atmos.append(resj["bodies"][index]["atmosphereComposition"][i])
            atmcp.append(0.25)
        case "Argon":
            atmos.append(resj["bodies"][index]["atmosphereComposition"][i])
            atmcp.append(0.93)
        case _:
            atmos.append(resj["bodies"][index]["atmosphereComposition"][i])
            atmcp.append(1)

print(len(atmos))

if len(atmos) < 3:
    atmos.append(3)
    atmcp.append(1)

compo1 = resj["bodies"][index]["solidComposition"]["Rock"]
compo2 = resj["bodies"][index]["solidComposition"]["Metal"]

rotper = resj["bodies"][index]["rotationalPeriod"]

massDif =   100 - (abs(1 - mass)        / ((1 + mass)        / 2)) * difRatio * 100
radiusDif = 100 - (abs(6378.1 - radius)   / ((6378.1 + radius)   / 2)) * difRatio * 100
gravityDif =100 - (abs(0.9999686429450564 - gravity) / ((0.9999686429450564 + gravity) / 2)) * difRatio * 100
tempDif =   100 - (abs(288 - temp)   / ((288 + temp)   / 2)) * difRatio * 100
presDif =   100 - (abs(0.9990787688132248 - pres)        / ((0.9990787688132248 + pres)        / 2)) * difRatio * 100
atmos1Dif = 100 - (abs(atmcp[0] - atmos[0])   / ((atmcp[0] + atmos[0])   / 2)) * difRatio * 100
atmos2Dif = 100 - (abs(atmcp[1] - atmos[1])   / ((atmcp[1] + atmos[1])   / 2)) * difRatio * 100
atmos3Dif = 100 - (abs(atmcp[2] - atmos[2])   / ((atmcp[2] + atmos[2]) / 2)) * difRatio * 100
compo1Dif = 100 - (abs(70.0 - compo1)   / ((70.0 + compo1)   / 2)) * difRatio * 100
compo2Dif = 100 - (abs(30.0 - compo2)   / ((30.0 + compo2)   / 2)) * difRatio * 100
rotperDif = 100 - (abs(0.997269752199074 - rotper)      / ((0.997269752199074 + rotper)      / 2)) * difRatio * 100

print("It is " + str(round(((massDif+radiusDif+gravityDif+tempDif+presDif+atmos1Dif+atmos2Dif+atmos3Dif+compo1Dif+compo2Dif+rotperDif)/11), 2)) + "% like Earth",end="")

if body == "Earth":
    print(" (Shocker!)")
else:
    print("")