###########################################################
############### Author - Balaji Ravi ######################
###########################################################

import requests, json
from datetime import date

#Using API For authentication
api_key = "05d6694161fcb0b6acea7621170265c5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

n = int(input("Enter the number of response you want"))
list = []
for i in range (0,n):
    city_names = input("Enter city name : ")
    list.append(city_names)

for i in range(0,n):
    city_name = ''
    city_name = list[i]
#Framing the URL For requests package
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    # Storing the json values in a variable
    x = response.json()

    #If the return code is not 404, process the data else throw error to user
    if x["cod"] != "404":
    
# 	getting the required datas
        y = x['main']
        c = x['sys']
        w = x['wind']
        temperature = y["temp"]
        pressure = y["pressure"]
        humidiy = y["humidity"]
        min_temp = y['temp_min']
        max_temp = y['temp_max']
        z = x["weather"]  
        coordinates = x['coord']
        name = x['name']
        weather= z[0]["description"]
        country = c['country']
        wind_speed = w['speed']
        wind_deg = w['deg']
    
	#Opening a file and writting the datas onto the file
        
	f = open("weather_data.doc",'a',encoding = 'utf-8')
        f.write("\n")
	f.write(str(name) + "\t" + str(country) +"\t" + str(weather) + '\t' + str(min_temp) +'\t' + str(max_temp) +'\t'+ 
        str(pressure) +'\t' + str(humidiy) +'\t' + str(wind_speed) +'\t' + str(wind_deg) +'\t' + str(coordinates) +'\t' + str(date.today()) +'\n')
        f.close()
        print("Write Sucessful")
    else:
        print(" City Not Found ")
		
