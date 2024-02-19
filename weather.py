import requests
from bs4 import BeautifulSoup
def getWeather(city):
    # url and requests
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    # Fetching data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    #other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]


    # returning data
    return (f"The temperature of {city} is {temp} and sky condition is {sky} on {time}")

#Handling Exception 
try:
    city=input("Enter the Name of city to check weather:- ")
    print(getWeather(city))
except Exception as e:
    print(f"City not found!. Please write the valid city")
