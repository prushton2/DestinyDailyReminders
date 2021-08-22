from lxml import html
import requests
import json
import os

jsm = __import__("jsonmanager")
jsonmanager = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))
apiKey = jsonmanager.load()["apiKey"]

getVendors = __import__("getvendors")

def compareCollections(userInformation, mods):

    dictionary_url = "https://raw.githubusercontent.com/prushton2/DestinyCollections/master/dict.json" #Grabs the dictionary from github
    res = requests.get(dictionary_url)
    dictionary = json.loads(res.text)
    
    HEADERS=  {
        "X-API-Key": apiKey
    }

    membershipType, destinyMembershipId, characterId = userInformation[0], userInformation[1], userInformation[2]

    url = f"https://bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=800"

    res = requests.get(url, headers=HEADERS)

    collections = json.loads(res.text)["Response"]["profileCollectibles"]["data"]["collectibles"]

    itemsUserDoesntHave = []

    for i in mods:
        if(collections[i]["state"]%2 == 1): #read if user DOESNT have item
            itemsUserDoesntHave.append(i)

    for i, item in enumerate(itemsUserDoesntHave):
        itemsUserDoesntHave[i] = dictionary[item]
    
    return itemsUserDoesntHave
