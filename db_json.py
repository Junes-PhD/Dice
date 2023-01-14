import json

with open('characters.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print(data['INTERCESSION SQUAD']["INTERCESSOR SERGEANT"]["Shooting"])


'''
intercessor_squad = {
    "M": 6,
    "WS": 3,
    "BS": 3,
    "S": 4,
    "T": 4,
    "W": 2,
    "A": 2,
    "Ld": 7,
    "Sv": 3,
    "Shooting": "Bolt Riftle",
    "Melee": "Knife",
}
int_army= {"intercessor sqaud":intercessor_squad}
squad = {"Intercessors":int_army}

with open("characters.json", "w") as outfile:
    json.dump(squad, outfile)
'''