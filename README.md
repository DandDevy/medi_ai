# Medi_ai

## Explanation
This is a flask server with a hosting file for keras models.
These keras models are for predicting diabetes, cancer, heart disease, etc

## Requirments
requires tensorflow and flask

To run use python with anaconda.

## Local
To run locally use python main.py
then go to http://localhost:5002/

## Remote
To run remotely use python host.py while a VM for example.
then go to https://medi-ai.serveo.net

### WARNING THIS MAY ALREADY BE IN USE. 
If that is the case, inside of host.py you can change the constant SITE_NAME.
You can change SITE_NAME = "medi-ai" to SITE_NAME = "WHATEVER_YOU_WANT"
Then go to https://WHATEVER_YOU_WANT.serveo.net
