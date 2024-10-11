from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import *

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    print(response)
    return """For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.""".format(
        response['anger'],response['disgust'],response['fear'],response['joy'],response['sadness'],
        response['dominant_emotion'])


@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)