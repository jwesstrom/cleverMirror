try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import requests



def createTree(url):
	data = requests.get(url, stream=True)
	root = ET.fromstring(data.text.encode("utf-8"))
	return root


url = 'http://api.sl.se/api2/realtimedepartures.xml?key=11bda0da60e24b938d5a3e3cca3b09c1&siteid=9141&timewindow=600'
root = createTree(url)
ns = '{http://sl.se/Departures.xsd}'
metroCollection = []
for ResponseData in root.iter('ResponseData'):
    for Metros in ResponseData.iter(ns+'Metros'):
        for metroData in Metros:
            for i in metroData:
                if i.tag == ns+'JourneyDirection' and i.text == '1':
                    metroCollection.append(metroData)
metroPrintList = []
for i in metroCollection:
    for b in i:
        if b.tag == ns+'DisplayTime':
            metroPrintList.append(b.text)
            if b.tag == ns+'Destination':
                metroPrintList.append('Mot ' + b.text.encode("utf-8"))
print metroPrintList


print createTree(url)
