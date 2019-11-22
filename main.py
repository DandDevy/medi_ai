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

# import host_with_ngrok
from Logger import Logger

LOCAL_PORT_NUMBER = "5002"

HOST_ADDRESS = "0.0.0.0"
LOCAL_ADDRESS = "localhost"

app = Flask(__name__)

diabetes_model = load_model("diabetes_8255.h5")
prostate_cancer_model = load_model("my_prostate_cancer_model.h5")
breast_cancer_model = load_model("my_breast_cancer_model.h5")
heart_model = load_model("my_heart_model.h5")

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
	logger = Logger()
	user_ip = request.remote_addr
	log_type = "tfversion=" + str(tfversion)
	logger.log(log_type, user_ip)

	return tfversion

@app.route("/heart")
def heart():
	try:
		val0 = request.args.get("val0")
		val1 = request.args.get("val1")
		val2 = request.args.get("val2")
		val3 = request.args.get("val3")
		val4 = request.args.get("val4")
		val5 = request.args.get("val5")
		val6 = request.args.get("val6")
		val7 = request.args.get("val7")
		val8 = request.args.get("val8")
		val9 = request.args.get("val9")
		val10 = request.args.get("val10")
		val11 = request.args.get("val11")
		val12 = request.args.get("val12")
		IsRound = request.args.get("round")

		# heart?val0=52&val1=1&val2=0&val3=125&val4=212&val5=0&val6=1&val7=168&val8=0&val9=1&val10=2&val11=2&val12=3 returns 0.040595107

		#http://309ce189.ngrok.io/heart?val0=52&val1=1&val2=0&val3=125&val4=212&val5=0&val6=1&val7=168&val8=0&val9=1&val10=2&val11=2&val12=3&round=1 returns 0


		single_x_test = [int(val0), int(val1), int(val2), int(val3), int(val4), int(val5) , int(val6), int(val7), int(val8), int(val9), int(val10), int(val11), int(val12)]
		# single_x_test = [71,0,0,112,149,0,1,125,0,1.6,1,0,2] returns 0.7353674
		bigRes = heart_model.predict(np.array([single_x_test]))
		res = bigRes[0][0]


		logger = Logger()
		user_ip = request.remote_addr
		log_type = "heart={ input="+str(single_x_test) + ", res=" + str(res) + "}"
		logger.log(log_type, user_ip)

		if IsRound == "1":
			res = round(float(res))

		return str(res)

	except Exception as e:
		return str(e)

@app.route("/breast_cancer")
def breast_cancer():
	try:
		val0 = request.args.get("val0")
		val1 = request.args.get("val1")
		val2 = request.args.get("val2")
		val3 = request.args.get("val3")
		val4 = request.args.get("val4")
		IsRound = request.args.get("round")

		# breast_cancer?val0=17.99&val1=10.38&val2=122.8&val3=1001&val4=0.1184 returns 0.0068584555
		# breast_cancer?val0=17.99&val1=10.38&val2=122.8&val3=1001&val4=0.1184&round=1 returns 0

		single_x_test = [float(val0),float(val1),float(val2),int(val3),float(val4)]
		bigRes = breast_cancer_model.predict(np.array([single_x_test]))
		res = bigRes[0][0]

		if IsRound == "1":
			res = round(float(res))

		logger = Logger()
		user_ip = request.remote_addr
		log_type = "breast_cancer={ input="+str(single_x_test) + ", res=" + str(res) + "}"
		logger.log(log_type, user_ip)

		return str(res)

	except Exception as e:
		return str(e)


@app.route("/prostate_cancer")
def prostate_cancer():
	try:

		val0 = request.args.get("val0")
		val1 = request.args.get("val1")
		val2 = request.args.get("val2")
		val3 = request.args.get("val3")
		val4 = request.args.get("val4")
		val5 = request.args.get("val5")
		val6 = request.args.get("val6")
		val7 = request.args.get("val7")
		val8 = request.args.get("val8")
		IsRound = request.args.get("round")

		# prostate_cancer?val0=1&val1=23&val2=12&val3=151&val4=954&val5=0.143&val6=0.51&val7=0.2&val8=0.010  returns   0.7160286

		# prostate_cancer?val0=1&val1=23&val2=12&val3=151&val4=954&val5=0.143&val6=0.51&val7=0.2&val8=0.010&round=1 returns 1

		single_x_test = [int(val0), int(val1), int(val2), int(val3), int(val4), float(val5), float(val6), float(val7), float(val8)]
		BigRes = prostate_cancer_model.predict(np.array([single_x_test]))
		res = BigRes[0][0]

		if IsRound == "1":
			res = round(float(res))

		logger = Logger()
		user_ip = request.remote_addr
		log_type = "prostate_cancer={ input="+str(single_x_test) + ", res=" + str(res) + "}"
		logger.log(log_type, user_ip)

		return str(res)

	except Exception as e:
		return str(e)


@app.route("/diabetes")
def diabetes():
	try:
		va0 = request.args.get("val0")
		print("VAL0:", va0)
		va1 = request.args.get("val1")
		va2 = request.args.get("val2")
		va3 = request.args.get("val3")
		va4 = request.args.get("val4")
		va5 = request.args.get("val5")
		va6 = request.args.get("val6")
		va7 = request.args.get("val7")
		IsRound = request.args.get("round")

		# http://localhost:5002/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=70         returns    0.30901816
		#http://localhost:5002/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=50&round=1  returns 0
		#http://localhost:5002/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=30&round=1  returns 1

		# single_x_test = [1,163,71,35,0,33.0,0.627,70]
		# single_x_test = [int(val0),163,71,35,0,33.0,0.627,70]
		single_x_test = [int(va0), int(va1), int(va2), int(va3), int(va4), float(va5), float(va6), int(va7)] #http://localhost:5002/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=70
		q = diabetes_model.predict(np.array([single_x_test]))
		res = q[0][0]
		#     print(q[0][0])
		#     qstring = q.tostring()
		#     print(qstring)

		if IsRound == "1":
			res = round(float(res))

		logger = Logger()
		user_ip = request.remote_addr
		log_type = "diabetes={ input="+str(single_x_test) + ", res=" + str(res) + "}"
		logger.log(log_type, user_ip)

		return str(res)
	except Exception as e:
		return str(e)



@app.route("/index")
def index():
	logger = Logger()
	user_ip = request.remote_addr
	logger.log("index", user_ip)
	return render_template("index.html")

@app.route("/log")
def log():
	# return "asd"
	try:
		logger = Logger()
		user_ip = request.remote_addr
		return logger.read()
	except Exception as e:
		return str(e)


if __name__ == '__main__':
	print("Starting...")
	# host_with_ngrok.inform_website_of_site_name_change()
	app.debug = False
	app.run(host=LOCAL_ADDRESS, port=LOCAL_PORT_NUMBER)
