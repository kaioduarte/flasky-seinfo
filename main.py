from flask import Flask, render_template, abort
import requests

TOKEN = "d1b66cf1ff402681b9a0ae2c26393f46b468f267"
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route("/perfil/<string:username>")
def perfil(username):
	URL = "https://api.github.com/users/{0}?access_token={1}".format(username, TOKEN)
	response = requests.get(URL)
	content = response.json()
	if response.status_code == 200:
		repos_url = content["repos_url"]
		repos = requests.get(repos_url).json()
		return render_template("perfil.html", usuario=content, repos=repos)
	else:
		abort(404)


if __name__ == '__main__':
	app.run(debug=True)
