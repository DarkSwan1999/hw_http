import requests

heroes = ["Hulk", "Captain America", "Thanos"]
intelligence_score = {}

response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
data = response.json()

for hero in heroes:
    for i in range(len(data)):
        if data[i]["name"] == hero:
            intelligence_score[hero] = int(data[i]["powerstats"]["intelligence"])

smart_hero = max(intelligence_score, key=intelligence_score.get)

with open("json_api.txt",'w') as file:
    for hero in heroes:
        file.write(hero + " intelligence: " + str(intelligence_score[hero]) + "\n")
    file.write("Smart Hero: " + smart_hero + " with intelligence score " + str(intelligence_score[smart_hero]))

print("Smart Hero: " + smart_hero + " with intelligence score " + str(intelligence_score[smart_hero]))