import http.client, urllib.parse, urllib.error
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f7cc29509a8443c5b3a5e56b0e38b5a6'
}

params = urllib.parse.urlencode({
    # Request parameters
    'expr': 'Id=2140251882',
    'count': '10',
    'attributes': 'Id,AA.AuId,AA.AfId',
})

conn = http.client.HTTPSConnection('oxfordhk.azure-api.net')
conn.request("GET", "/academic/v1.0/evaluate?%s" % params, None, headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
