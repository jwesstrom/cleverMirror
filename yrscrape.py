try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import requests


url = 'http://www.yr.no/place/Sweden/Stockholm/Bagarmossen/forecast.xml'
data = requests.get(url, stream=True)
root = ET.fromstring(data.text.encode("utf-8"))

for forecast in root.iter('forecast'):
	c = 0
	for time in forecast[0]:
		c = c + 1
		if c < 4:
			for i in time:
				if i.tag == 'symbol':
					print time.attrib
		else:
			break
