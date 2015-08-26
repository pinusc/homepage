import urllib.request
from datetime import datetime, date, timedelta
from json import loads
from flask import Flask
from flask import render_template
import subprocess
app = Flask(__name__)
static = 'static/'
@app.route("/")
def hello():
	fortune = subprocess.check_output('fortune -s', shell=True, universal_newlines=True)
	fortune = fortune.replace('"', '\\"')
	cow = subprocess.check_output('cowsay -f $(ls /usr/share/cows|  shuf -n1) "%s"' % (fortune), shell=True, universal_newlines=True)
	
	json = get_weather()
	days = []
	for i in range(4):
		sky = json['list'][i]["weather"][0]['id']
		if sky == 800:
			sky_icon = static + 'weather_sunny' + ".png"
		else:
			sky_type = sky // 100
			sky_array = [None, 
						None, 
						'thunder', 
						None, 
						None, 
						'rain', 
						'snow', 
						'fog',
						'cloud']
			sky_icon = static + 'weather_' + sky_array[sky_type] + '.png'
		wdate = datetime.fromtimestamp(json['list'][i]['dt']).date()
		if wdate == date.today():
			wdate = 'Today'
		elif wdate == date.today() + timedelta(days=1):
			wdate = 'Tomorrow'
		else: 
			wdate = wdate.strftime("%m-%d")
		days.append({
			'day': wdate,
			'sky': sky_icon,
			'temperature': json['list'][i]['temp']['day'],
			'wind': json['list'][0]['speed'] * 3.6,
			})

	return render_template('home.html', cowsay=cow, forecast=days)

def get_weather():
	response = urllib.request.urlopen(
		'http://api.openweathermap.org/data/2.5/forecast/daily?q=foggia,it&cnt=4&units=metric')
	text = response.read().decode("utf-8")
	json = loads(text)
	return json


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')