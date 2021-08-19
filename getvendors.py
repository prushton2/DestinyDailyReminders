from lxml import html
import requests
import json
import os

jsm = __import__("jsonmanager")
jsonmanager = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))
apiKey = jsonmanager.load()["apiKey"]

HEADERS = {"X-API-Key": apiKey}
vendorHashes = []

def getVendorData(membershipType, destinyMembershipId, characterId):
    responseData = []
    # for i in range()
    url = f"https://bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/?components=308"
    res = requests.get(url, headers=HEADERS)
    responseData.append(res.text)

    # for i in vendorHashes:
    #     url = f"bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{i}/"
    #     res = requests.get(url, headers=HEADERS)
    #     responseData.append(res.text)

    return responseData
