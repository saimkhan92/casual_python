import urllib.request
import json
import webbrowser

address=input("Enter the address to search restaurants\n")
address=address.replace(" ","+")

# extract lat and long using google API

url= "https://maps.googleapis.com/maps/api/geocode/json?address="+address
response= urllib.request.urlopen(url)
data=response.read().decode("utf-8")
data1 = json.loads(data)
latitude=str(data1["results"][0]["geometry"]["location"]["lat"])
print(latitude)
longitude=str(data1["results"][0]["geometry"]["location"]["lng"])
print(longitude)
print("GPS coordinates are {} lat and {} lon".format(latitude,longitude))

# Extract listt of Cuisines from Zomato

url2="https://developers.zomato.com/api/v2.1/cuisines?lat="+latitude+"&lon="+longitude

req = urllib.request.Request(url2)
req.add_header('Accept', 'application/json')
req.add_header('user-key', '6e5c2bd0b09bc348bb6a0c8aef52e72d')
response = urllib.request.urlopen(req)
content = response.read().decode("utf-8")
#print(content)
content1= json.loads(content)
#print(content1["cuisines"][1])

for dic in content1["cuisines"]:
    print(dic["cuisine"]["cuisine_name"])

# Display restaurant

selected_cuisine=input("\nPlease choose from the following cuisines available at your location\n")
selected_cuisine=selected_cuisine.replace(" ","+")
url3="https://developers.zomato.com/api/v2.1/search?count=1&lat="+latitude+"&lon="+longitude+"&cuisines="+selected_cuisine+"&sort=rating&order=asc"

req = urllib.request.Request(url3)
req.add_header('Accept', 'application/json')
req.add_header('user-key', '6e5c2bd0b09bc348bb6a0c8aef52e72d')
response = urllib.request.urlopen(req)
content = response.read().decode("utf-8")
content= json.loads(content)

print("\nThe Best Restaurant is:\n")

print(content["restaurants"][0]["restaurant"]["name"]+", located at "+content["restaurants"][0]["restaurant"]["location"]["address"])

option=input("\nWould you like to see the menu card? Y or N\n")

if option=="Y"or"y":
    webbrowser.open(content["restaurants"][0]["restaurant"]["url"])

print("\nThank you!\n")




