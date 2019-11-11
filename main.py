"""
author: Daniel Ashcroft
purpose: run a flask server for use machine learning models
"""
from flask import Flask,render_template,request,url_for
#EDA Packages
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

LOCAL_PORT_NUMBER = "5002"

HOST_ADDRESS = "0.0.0.0"
LOCAL_ADDRESS = "localhost"

app = Flask(__name__)

diabetes_model = load_model("diabetes_8255.h5")

@app.route("/")
def doc():
	return render_template("doc.html")

@app.route("/arg")
def testArgs():
	language = request.args.get('language')#if key doesn't exist, returns None
	framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
	website = request.args.get('website')
	# better to use request.args.get(...) to avoid 400
	#  they are of type str

	# diabetes_model = tf.keras.models.load_model("diabetes_model.h5")
	# diabetes_model.summary()

	return '''<h1>The language value is: {}</h1>
				<h1>The framework value is: {}</h1>
			  <h1>The website value is: {}'''.format(language, framework, website)

@app.route("/tfversion")
def tfversion():
	tfversion = tf.__version__
	return tfversion

@app.route("/diabetes")
def diabetes():
	va1 = request.args.get("vall")
	single_x_test = [1,168,71,35,0,33.6,0.627,70]
	q = diabetes_model.predict(np.array([single_x_test, ]))
	res = q[0][0]
	#     print(q[0][0])
	#     qstring = q.tostring()
	#     print(qstring)
	return str(res)


@app.route("/index")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	print("Starting...")
	app.debug = False
	app.run(host=LOCAL_ADDRESS, port=LOCAL_PORT_NUMBER)
