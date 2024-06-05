
import urllib.parse
import requests


main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
address='lhr'
url = main_api + urllib.parse.urlencode({'address': address})
response=requests.get(url)
data=response.json()


print(data)