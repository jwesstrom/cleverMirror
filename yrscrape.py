try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import requests


url = 'http://www.yr.no/place/Sweden/Stockholm/Bagarmossen/forecast.xml'
data = requests.get(url, stream=True)
root = ET.fromstring(data.text.encode("utf-8"))

forecastList = []

for forecast in root.iter('forecast'):
    c = 0
    for time in forecast[0]:
        c = c + 1
        if c < 4:
            tTime = time.attrib['from'].split('T')[-1][:5] + '-' + time.attrib['to'].split('T')[-1][:5]
            tTemperature = time.find('temperature').attrib['value']
            tSymbol = time.find('symbol').attrib['number']
            tName = time.find('symbol').attrib['name']
            tempList = [tTime, tTemperature, tName, tSymbol]
            forecastList.append(tempList)
        else:
            break
#
# print forecastList[0].find('symbol').attrib['number']
# print forecastList[0].find('symbol').attrib['name']
# print forecastList[0].find('temperature').attrib['value']
# print forecastList[0].attrib['to'].split('T')[-1][:5]
# print forecastList[0].attrib['from'].split('T')[-1][:5]
print forecastList
