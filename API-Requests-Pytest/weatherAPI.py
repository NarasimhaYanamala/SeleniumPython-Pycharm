''''
basic : to paint a car we need tools like paint bottle and brush. Similar way libraries are tool like to develop code
'''

import json
import requests
import jsonpath   # jsonpath package install
from jsonpath import jsonpath
## API to fetch temp of city
##city_name=input('Enter City name')
city_name='London'
api_key='030075b0fc5413c08ad2663004be0d5a'

#f is used to keep the format
#adding units=metric to the url using &
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(api_url)
data=response.json()
print(data)      #### Data is python object it has to be convert to readable json ( Serialization)

# For pretty formatting the json data
pretty_data=json.dumps(data,indent=4)  ## it helps us to understand but not needed for code
print(pretty_data)


# To Fetch specific data
#method:1
D=data["weather"][0]['description']
T=data["main"]["temp"]
print(D,T)
print(f'The current weather is: {D} & Temp is: {T}')

# To Fetch Using JSONPATH


