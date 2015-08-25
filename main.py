from flask import Flask
from flask import render_template
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
	try:
		fortune = subprocess.check_output('fortune -s -o', shell=True, universal_newlines=True)
		fortune = fortune.replace('"', '\\"')
		cow = subprocess.check_output('cowsay -f $(ls /usr/share/cows|  shuf -n1) "%s"' % (fortune), shell=True, universal_newlines=True)
	except Exception as e:
		return str(e)
	return render_template('home.html', cowsay=cow)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')