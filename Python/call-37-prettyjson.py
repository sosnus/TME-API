from urllib.parse import urlencode
import json
import requests

url = "https://api.tme.eu/Products/GetPrices.json"

reqbody = {
    'Country': 'PL',
    'Currency': 'PLN',
    'Language': 'PL',
    'SymbolList[0]': 'NE555D',
    'SymbolList[1]': '1N4007-DC',
    'Token': '<TME_TOKEN_HERE>',
    'ApiSignature': '<TME_SIGNATURE_AFTER_ENCODING_HERE>',
}


payload = urlencode(reqbody)
headers = {'Content-Type': "application/x-www-form-urlencoded"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

your_json = response.text
parsed = json.loads(your_json)
print(json.dumps(parsed, indent=4, sort_keys=True))
