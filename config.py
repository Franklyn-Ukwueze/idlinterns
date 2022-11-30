import os

basedir = os.path.abspath(os.path.dirname(__file__))

# creating a configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') 

#BASE_URI = os.environ.get('BASE_URI') 
SAFEPAY_URI = os.getenv('SAFEPAY_URI')
print(SAFEPAY_URI)
API_KEY = os.getenv('API_KEY')
print(API_KEY) 
#MONGO_URI = os.environ.get('MONGO_URI') 
USSD_username = os.getenv('USSD_username')
print(USSD_username) 
USSD_api_key = os.getenv('USSD_api_key') 
print(USSD_api_key)
