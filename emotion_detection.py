import requests
import json
def emotion_detector(text_to_analyse):
    try:
        url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
        myobj = { "raw_document": { "text": text_to_analyse } } 
        header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
        response = requests.post(url, json = myobj, headers=header)  
        json_response = json.loads(response.text)
        return json_response['documentSentiment']['label']
    except Exception as ex:
        return 'Error'