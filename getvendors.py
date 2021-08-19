from lxml import html
import requests
import json
import os

HEADERS = {}

vendorHashes = [0]

def getVendorData(membershipType, destinyMembershipId, characterId):
    responseData = []

    url = f"bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{i}/"


    for i in vendorHashes:
        url = f"bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{i}/"
        res = requests.get(url, headers=HEADERS)
        responseData.append(res.text)

    return responseData
