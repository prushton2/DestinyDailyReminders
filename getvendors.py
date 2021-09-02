import requests
import json
import os

jsm = __import__("jsonmanager")
jsonmanager = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))

def getVendorData(message): #Takes the message itself (not text)

    vendordict = message.embeds[0].to_dict() #Converts the embed from Charlemagne to a dict
    
    if(vendordict["title"] == "Banshee-44, Gunsmith"): #If bansheee, get the mods

        mods = vendordict["fields"][4]["value"].split("\n")

    if(vendordict["title"] == "Ada-1, Armor Synthesis"): #If ada, get the mods

        mods = vendordict["fields"][1]["value"].split("\n")

    for i, mod in enumerate(mods): #Gets rid of the type of mod, leaving only the name so it can be indexed in the dictionary
        mods[i] = mod.split(",")[0]

    dictionary_url = "https://raw.githubusercontent.com/prushton2/DestinyCollections/master/dict.json" #Grabs the dictionary from github
    res = requests.get(dictionary_url)
    dictionary = json.loads(res.text)
    responseData = []
     
    for i in mods: #Indexes the mod in the dictionary to get the hash from the name.
        for j in dictionary:
            if(dictionary[j] == i):
                responseData.append(j)

    return responseData, vendordict["title"].split(",")[0]
