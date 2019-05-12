from urllib import request, parse

reqbody = {
    'Country': 'PL',
    'Currency': 'PLN',
    'Language': 'PL',
    'SymbolList[0]': 'NE555D',
    'SymbolList[1]': '1N4007-DC',
    'Token': '<TME_TOKEN_HERE>',
    'ApiSignature': '<TME_SIGNATURE_AFTER_ENCODING_HERE>',
}

data = parse.urlencode(reqbody).encode()
req = request.Request('https://api.tme.eu/Products/GetPrices.json', data)
resp = request.urlopen(req)

print(resp.read())