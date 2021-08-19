from lxml import html
import requests
import json
import os

jsm = __import__("jsonmanager")
jsonmanager = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))
apiKey = jsonmanager.load()["apiKey"]

getVendors = __import__("getvendors")

def compareCollections(userInformation):
    
    membershipType, destinyMembershipId, characterId = userInformation[0][0], userInformation[0][1], userInformation[0][2]

    vendorInfo = getVendors.getVendorData(membershipType, destinyMembershipId, characterId)

    for i in userInformation:
        membershipType, destinyMembershipId, characterId = userInformation[i][0], userInformation[i][1], userInformation[i][2]
