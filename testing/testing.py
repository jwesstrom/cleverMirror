try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import requests


class webScraper(object):
    # def __init__(self, service):
    #     self.service = service

    def createTree(url):
        # if self.service == 'sl':
        #     url = 'http://api.sl.se/api2/realtimedepartures.xml?key=11bda0da60e24b938d5a3e3cca3b09c1&siteid=9141&timewindow=60'
        # elif self.service == 'yr':
        #     url = 'http://www.yr.no/place/Sweden/Stockholm/Bagarmossen/forecast.xml'
    	data = requests.get(url, stream=True)
    	root = ET.fromstring(data.text.encode("utf-8"))
    	return root

    def slMetroDeparture():
        url = 'http://api.sl.se/api2/realtimedepartures.xml?key=11bda0da60e24b938d5a3e3cca3b09c1&siteid=9141&timewindow=60'
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
    	return metroPrintList

    def weather(self):
        root = self.createTree()
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
        return forecastList



# print slMetroDeparture(createTree(slBagarmossen))
# print weather(createTree(yrBagarmossen))

print webScraper().slMetroDeparture
#print webScraper('yr').weather()
