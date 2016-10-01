from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.environ.get("PORT", None))