from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        unit = request.POST['unit']
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=344c47d4dc1675639c6b1bc61e8425a9').read()

        list_data = json.loads(source)

        temp_k = list_data['main']['temp']
        if unit == 'C':
            temp = str(temp_k - 273.15) + 'C'
        elif unit == 'F':
            temp = str((temp_k - 273.15) * 9/5 + 32) + 'F'
        else:
            temp = str(temp_k) + 'K'        

        country_code = str.lower(list_data['sys']['country'])
        flag_url = "https://cdn.kcak11.com/CountryFlags/countries/"+ country_code +".svg"    

        print(list_data)
        data = {
            "country_code":str(list_data['sys']['country']),
            "coordinate":str(list_data['coord']['lon']) + ' , ' + str(list_data['coord']['lat']),
            "temp":temp,
            "pressure":str(list_data['main']['pressure']),
            "humidity":str(list_data['main']['humidity']),  
            "flag_url":flag_url,
        }
        print(data)
    else:
        data = {}
    return render(request,'index.html',data)        