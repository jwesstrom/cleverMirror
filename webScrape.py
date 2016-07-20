try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import requests


class webScraper(object):
    def createTree(self, url):
    	data = requests.get(url, stream=True)
    	root = ET.fromstring(data.text.encode("utf-8")) #without encode('utf-8') it will error. I think it's because ElementTree is written in c, and sends unicode in a way python does not understand.
    	return root

    def slMetroDeparture(self):
        url = 'http://api.sl.se/api2/realtimedepartures.xml?key=11bda0da60e24b938d5a3e3cca3b09c1&siteid=9141&timewindow=60'
    	root = self.createTree(url)
    	ns = '{http://sl.se/Departures.xsd}' #the xml has some werid name space stuff, so all the tags/elements below ResponseData prints with {http://sl.se/Departures.xsd} before the nametag.
    	metroCollection = []
    	for ResponseData in root.iter('ResponseData'):
    		for Metros in ResponseData.iter(ns+'Metros'):
    			for metroData in Metros:
    				for i in metroData:
    					if i.tag == ns+'JourneyDirection' and i.text == '1': #checks the direction of the train, and if it is 1 (heading from skarpnaeck), it appends the metro object to the collection
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
        url = 'http://www.yr.no/place/Sweden/Stockholm/Bagarmossen/forecast.xml'
        root = self.createTree(url)
        forecastList = []

        for forecast in root.iter('forecast'):
            c = 0
            for time in forecast[0]:
                c = c + 1 # the counter stops afer three cycles. Because I only want three forecasts
                if c < 4:
                    tTime = time.attrib['from'].split('T')[-1][:5] + '-' + time.attrib['to'].split('T')[-1][:5]
                    tTemperature = time.find('temperature').attrib['value']
                    tSymbol = time.find('symbol').attrib['number']
                    tName = time.find('symbol').attrib['name']
                    tempList = [tTime, tName, tTemperature, tSymbol]
                    forecastList.append(tempList)
                else:
                    break
        return forecastList

#print webScraper().slMetroDeparture()
#print webScraper().weather()
