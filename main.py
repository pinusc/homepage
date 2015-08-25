from flask import Flask
from flask import render_template
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
	try:
		fortune = subprocess.check_output('fortune -s', shell=True, universal_newlines=True)
		cow = subprocess.check_output('echo "%s" | cowsay -f $(ls /usr/share/cows|  shuf -n1)' % (fortune), shell=True, universal_newlines=True)
	except Exception as e:
		print(e)
	return render_template('home.html', cowsay=cow)

if __name__ == "__main__":
    app.run(debug=True)