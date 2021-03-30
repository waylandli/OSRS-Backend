from flask import Flask
from flask_restful import abort
import requests
import csv
import io
import json

app = Flask(__name__)


@app.route("/<name>")
def get_hiscore(name):

    # OSRS Hiscores API endpoint
    BASE_URL = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='

    # Format of the Hiscores CSV file taken from another repo
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
                'Obor', 'Sarachnis', 'Scorpia', 'Skotizo', 'Tempoross', 'The Gauntlet', 'The Corrupted Gauntlet', 'Theatre of Blood',
                'Thermonuclear Smoke Devil', 'TzKal-Zuk', 'TzTok-Jad', 'Venenatis', "Vet'ion", 'Vorkath', 'Wintertodt',
                'Zalcano', 'Zulrah']

    # Empty Dictionary to hold in results
    data = {}

    # Make a call to Hiscores API
    response = requests.get(BASE_URL + name)
    if response.status_code == 404:
        abort(404, message="Name not found")
    r = response.content

    # Read CSV file line by line into dictionary with correct name
    num = 0
    s = io.StringIO(r.decode('utf-8'))
    csv_reader = csv.reader(s)
    for line in csv_reader:
        data[Hiscores[num]] = line
        num += 1

    # Creates JSON format
    json_data = json.dumps(data)

    return json_data


if __name__ == '__main__':
    app.run(debug=True)
