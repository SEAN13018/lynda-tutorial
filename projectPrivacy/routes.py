from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("/index.html")

@app.route("/navigation")
def navigation():
	return render_template("/navigation.html")
	
@app.route("/login")
def login():
	return render_template("/login.html")
	
@app.route("/help", methods=['GET', 'POST'])
def help():
	form = HelpForm()
	
	if request.method == 'POST':
		return "Success!"
	elif request.method == 'GET':
		return render_template("/help.html", form = form)
	
if __name__ == "__main__":
	app.run(debug=True)