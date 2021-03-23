from flask import Flask
import requests
import csv
import io
import json

app = Flask(__name__)


@app.route("/<name>")
def get_hiscore(name):

    # OSRS Hiscores API endpoint
    BASE_URL = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='

    Hiscores = ['Total', 'Attack', 'Defence', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic', 'Cooking',
                'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore',
                'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecrafting', 'Hunter', 'Construction',
                'League Points', 'Bounty Hunter - Hunter', 'Bounty Hunter - Rogue',
                'Clue Scrolls (all)', 'Clue Scrolls (beginner)', 'Clue Scrolls (easy)', 'Clue Scrolls (medium)',
                'Clue Scrolls (hard)', 'Clue Scrolls (elite)', 'Clue Scrolls (master)',
                'LMS - Rank', 'Soul Wars',
                'Abyssal Sire', 'Alchemical Hydra', 'Barrows Chests', 'Bryophyta', 'Callisto', 'Cerberus',
                'Chambers of Xeric', 'Chambers of Xeric: Challenge Mode', 'Chaos Elemental', 'Chaos Fanatic',
                'Commander Zilyana', 'Corporeal Beast', 'Crazy Archaeologist', 'Dagannoth Prime', 'Dagannoth Rex',
                'Dagannoth Supreme', 'Deranged Archaeologist', 'General Graardor', 'Giant Mole', 'Grotesque Guardians',
                'Hespori', 'Kalphite Queen', 'King Black Dragon', 'Kraken', "Kree'Arra", "K'ril Tsutsaroth", 'Mimic', 'Nightmare',
                'Obor', 'Sarachnis', 'Scorpia', 'Skotizo', 'The Gauntlet', 'The Corrupted Gauntlet', 'Theatre of Blood',
                'Thermonuclear Smoke Devil', 'TzKal-Zuk', 'TzTok-Jad', 'Venenatis', "Vet'ion", 'Vorkath', 'Wintertodt',
                'Zalcano', 'Zulrah']

    data = {}

    response = requests.get(BASE_URL + name).content

    s = io.StringIO(response.decode('utf-8'))
    num = 0

    csv_reader = csv.reader(s)
    for line in csv_reader:
        data[Hiscores[num]] = line
        num += 1

    json_data = json.dumps(data)
    print(json_data)

    return json_data


if __name__ == '__main__':
    app.run(debug=True)
