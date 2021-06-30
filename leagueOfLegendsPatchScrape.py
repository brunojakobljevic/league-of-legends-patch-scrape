import requests
import bs4

siteName = "https://na.leagueoflegends.com/en-us/news/game-updates/patch-{}-{}-notes/"
names = list()
namesDict = dict()

for n in range(9, 12):
    for m in range(1, 26):
        site = requests.get(siteName.format(str(n), str(m)))

        if "Error 404" in site.text:
            continue
        
        soup = bs4.BeautifulSoup(site.text, "lxml")
        
        imeChampa = soup.select("h3 > a")

        for item in imeChampa:
            names.append(item.text)

while(names != []):
    
    counter = 1
    i = 1
    
    while(i != len(names)):
        if names[0] == names[i]:
            counter += 1
            names.pop(i)
        else:
            i += 1
    else:
        namesDict.__setitem__(names[0], counter)
        names.pop(0)

maxValues = [0, 0, 0]

for key, value in namesDict.items():
    if value > maxValues[0]:
        maxValues[2] = maxValues[1]
        maxValues[1] = maxValues[0]
        maxValues[0] = value
        
for key, value in namesDict.items():
    for i in range(3):
        if value == maxValues[i]:
            print("Name: '{}', Frequency: {} \n".format(key, str(value)))
