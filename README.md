# Medi_ai

## Explanation
This is a flask server with a hosting file for keras models.
These keras models are for predicting diabetes, breast cancer, prostate cancer and heart disease.

## Requirments
requires tensorflow, flask and maybe ngrok if you choose to go that way.
To run use python with anaconda.

## Local
To run locally use python main.py
then go to http://localhost:5002/

## Remote
### Option 1 : serveo
To run remotely use python host.py while a VM for example.
then go to https://medi-ai.serveo.net

###### WARNING THIS MAY ALREADY BE IN USE. 
If that is the case, inside of host.py you can change the constant SITE_NAME.
You can change SITE_NAME = "medi-ai" to SITE_NAME = "WHATEVER_YOU_WANT"
Then go to https://WHATEVER_YOU_WANT.serveo.net

###### WARNING SOMETIMES SERVEO DOESN'T WORK
While it is easier to use, in November 2019 I personally no longer was able to use the service.

### Option 2 : ngrok
You must install and run ngrok, then run host_with_ngrok.py. It is set up so it will tell Fionn's 
website (medi-screen) when there has been a change of address.

## How to use

We use GETs to use to talk to this web server.

Example :
 
 http://localhost:5002/prostate_cancer?val0=1&val1=23&val2=12&val3=151&val4=954&val5=0.143&val6=0.51&val7=0.2&val8=0.010
 should return "0.7160286". 
 
 "localhost:5002" here can be replaced here.
 0.7160286 is a percentage between 0 and 1.
 We can add &round=1 to the end to get a rounded number.
  
 
http://localhost:5002/tfversion is really just for testing, it returns a 2.0.0 if success.

For the model communication, I will examples with dumby data so you can see the number of values, types of values
and play with them yourself.

http://localhost:5002/prostate_cancer?val0=1&val1=23&val2=12&val3=151&val4=954&val5=0.143&val6=0.51&val7=0.2&val8=0.010

for prostate cancer.

http://localhost:5002/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=7

for diabetes.

http://localhost:5002/breast_cancer?val0=17.99&val1=10.38&val2=122.8&val3=1001&val4=0.1184

for breast cancer.

http://localhost:5002/heart?val0=52&val1=1&val2=0&val3=125&val4=212&val5=0&val6=1&val7=168&val8=0&val9=1&val10=2&val11=2&val12=3

for heart disease.










