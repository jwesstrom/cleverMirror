# -*- coding: utf-8 -*-
# makes degree symbol possible
import urllib2

class yrScrape(object):
    def __init__(self, time):
        self.time = time
    def getWeather(self):

        weather = []


        data = urllib2.urlopen('http://www.yr.no/place/Sweden/Stockholm/Bagarmossen/')
        data = data.read().split('Today')[1].split('Tomorrow')[0]

        #read html page and keeps only the part that is for today

        dataList = []
        temperature = []
        time = []
        cloudCover = []
        timeTemperature = []

        for i in data.split('<tr>'):
            if '<td title="' in i:
                dataList.append(i)

        for i in dataList:
            timeTemperature = [] #resets the variable, as it should only keep current times temperature
            tempCloudCover = i.split('<td title=')[1].split('"')[1].split('.')[0]
            cloudCover.append(tempCloudCover)
            tempTimeTemp = i.split('<td class="temperature plus" title="')[1].split('"')[0]
        for b in tempTimeTemp.split(): #splits every whitespace
            if '\xc2\xb0' in b: #makes a split for every degree symbol
                timeTemperature.append(b.split('\xc2\xb0')[0])
                time.append(tempTimeTemp.split()[-1])
                temperature.append(timeTemperature)

        for i in range(len(time)):
            if temperature[i][0] == temperature[i][1]:
                temperature[i] = temperature[i][0] + '\xc2\xb0'
            else:
                temperature[i] = temperature[i][0] + '\xc2\xb0' + ' Känns som ' + temperature[i][1] + '\xc2\xb0' # if actual temperature and feels like is the same, it removes feels like

            #time.append(time[0]) #appends the first collected time, so that it loops and makes for 24h, to fix out of range error
            time.append('00:00') #appends 00:00 to the end, since that will always be the last entry on todays weather. ugly hack
            weatherTemp = time[i] + '-' + time[i+1] + ': ' + cloudCover[i] + ' ' +temperature[i]
            weather.append(weatherTemp)

        return weather[self.time]
