import mraa		#libray to inteact with the sensor
import time			#library to get time
import requests	#library to connect to api and get url
payload = {'key': 'fecc346b-a5c9-4e90-83cb-7616c2287641',
			'OperatorRef': 'MTA',
			'MonitoringRef': 502044,
			'LineRef': 'MTA NYCT_Q43'}
import pyupm_i2clcd as lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)



sensor_value = mraa.Gpio(4)
sensor_value.dir(DIR_IN)
senror_value.isr(mraa.Gpio(4), display_info, RISING)
#while True:

def display_info():
    results = requests.get('http://bustime.mta.info/api/siri/stop-monitoring.json', params = payload, verify = False)
		a = results.json()
		#location = []
		stops_away = []
		for stops in a['Siri']['ServiceDelivery']['StopMonitoringDelivery']:
			for e in stops['MonitoredStopVisit']:
				stops_away.append((e['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['StopsFromCall'],e['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']))
				#location.append((e['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],e['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))

		print stops_away

			#for word in message:
			#	port.write(word)
			#	time.sleep(1)
		for stops in stops_away:
			if stops[0] < 10:
				lcdDisplay.setColor(255,0,0)
			else:
				lcdDisplay.setColor(0,255,17)

			lcdDisplay.setCursor(0,0)
			lcdDisplay.write(str(stops[1]))
			lcdDisplay.setCursor(1,0)
			lcdDisplay.write('Q43')
			time.sleep(3)
			lcdDisplay.clear()
			lcdDisplay.setCursor(0,0)
		lcdDisplay.setCursor(0,0)
		lcdDisplay.write(str(stops_away[0][1]))
		lcdDisplay.setCursor(1,0)
		lcdDisplay.write('Q43')
			
			#time.sleep(40 - len(stops_away) * 3)
		time.sleep()

if True:
	lcdDisplay.setColor(0,0,0)
		
		
	#else:
		
	
		#lcdDisplay.setColor(0,0,0)
		
































