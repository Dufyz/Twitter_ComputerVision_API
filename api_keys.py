from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

def twitter_key():

    # Importando seeds do Twitter App

    api_key = ''
    api_key_secret = ''
    acess_token = ''
    acess_token_secret = ''

    return api_key, api_key_secret, acess_token, acess_token_secret

def azure_key():
    
    key = ''
    end_point = ''
    credential = CognitiveServicesCredentials(key)
    client = ComputerVisionClient(end_point, credential)

    return client