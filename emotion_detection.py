import requests 
import json
def emotion_detector(text_to_analyse):
    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        myobj = { "raw_document": { "text": text_to_analyse } } 
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        response = requests.post(url, json = myobj, headers=header)  
        json_response = json.loads(response.text)
        anger_score = json_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = json_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = json_response['emotionPredictions'][0]['emotion']['fear']
        sadness_score = json_response['emotionPredictions'][0]['emotion']['sadness']
        joy_score = json_response['emotionPredictions'][0]['emotion']['joy']
        max_score = max([anger_score,disgust_score,fear_score,sadness_score,joy_score])
        dominant_emotion = ''
        if max_score == anger_score:
            dominant_emotion = 'Anger'
        elif max_score == disgust_score:
            dominant_emotion = 'Disgust'
        elif max_score == fear_score:
            dominant_emotion = 'Fear'
        elif max_score == sadness_score:
            dominant_emotion = 'Sadness'
        elif max_score == joy_score:
            dominant_emotion = 'Joy'
        return {
            'anger': anger_score,'disgust': disgust_score,'fear': fear_score,
            'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion
            }
    except Exception as ex:
        print(ex)
        return 'Error'