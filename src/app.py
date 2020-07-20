from flask import Flask
from test import pre_process
app = Flask(__name__)

@app.route("/")
def hello():
	"""
	Initial setup for flask app
	:return:
	"""
	render_template()

if __name__=='__main__':
	app.run(host='0.0.0.0', port=1003, debug=True, threaded=True)